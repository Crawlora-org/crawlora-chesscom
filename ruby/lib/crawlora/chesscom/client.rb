require "json"
require "net/http"
require "uri"

module Crawlora
  module Chesscom
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"chesscom-club": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-club", "method": "GET", "params": [{"description": "Chess.com club URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/club/{slug}", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-club-matches": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-club-matches", "method": "GET", "params": [{"description": "Chess.com club URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/club/{slug}/matches", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-club-members": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-club-members", "method": "GET", "params": [{"description": "Chess.com club URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/club/{slug}/members", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-country": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-country", "method": "GET", "params": [{"description": "Two-character uppercase ISO country code or documented Chess.com region code", "in": "path", "name": "iso", "required": true, "type": "string", "x-example": "IT"}], "path": "/chesscom/country/{iso}", "pathParams": ["iso"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match", "method": "GET", "params": [{"description": "Positive Chess.com team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}], "path": "/chesscom/match/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match-board": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match-board", "method": "GET", "params": [{"description": "Positive Chess.com team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}, {"description": "Source board number", "in": "path", "name": "board", "required": true, "type": "integer"}], "path": "/chesscom/match/{id}/{board}", "pathParams": ["id", "board"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match-live": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match-live", "method": "GET", "params": [{"description": "Positive Chess.com live team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}], "path": "/chesscom/live-match/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match-live-board": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match-live-board", "method": "GET", "params": [{"description": "Positive Chess.com live team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}, {"description": "Source board number", "in": "path", "name": "board", "required": true, "type": "integer"}], "path": "/chesscom/live-match/{id}/{board}", "pathParams": ["id", "board"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-clubs": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-clubs", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/clubs", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-game-archives": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-game-archives", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/archives", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-game-month": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-game-month", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Four-digit game-end year", "in": "path", "name": "year", "required": true, "type": "string"}, {"description": "Game-end month, 1 through 12", "in": "path", "name": "month", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/archive/{year}/{month}", "pathParams": ["username", "year", "month"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-game-month-pgn": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-game-month-pgn", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Four-digit game-end year", "in": "path", "name": "year", "required": true, "type": "string"}, {"description": "Game-end month, 1 through 12", "in": "path", "name": "month", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/archive/{year}/{month}/pgn", "pathParams": ["username", "year", "month"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-games": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-games", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-games-to-move": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-games-to-move", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/to-move", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-is-online": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-is-online", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/is-online", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-live-games": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-live-games", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Base time in seconds", "in": "path", "name": "base_time", "required": true, "type": "integer"}, {"description": "Increment in seconds", "in": "path", "name": "increment", "required": true, "type": "integer"}], "path": "/chesscom/player/{username}/games/live/{base_time}/{increment}", "pathParams": ["username", "base_time", "increment"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-live-games-base-time": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-live-games-base-time", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Base time in seconds", "in": "path", "name": "base_time", "required": true, "type": "integer"}], "path": "/chesscom/player/{username}/games/live/{base_time}", "pathParams": ["username", "base_time"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-matches": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-matches", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/matches", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-stats": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-stats", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/stats", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-tournaments", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/tournaments", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-puzzle": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-puzzle", "method": "GET", "params": [], "path": "/chesscom/puzzle", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-puzzle-random": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-puzzle-random", "method": "GET", "params": [], "path": "/chesscom/puzzle/random", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-tournament": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-tournament", "method": "GET", "params": [{"description": "Chess.com tournament URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/tournament/{slug}", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-tournament-round": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-tournament-round", "method": "GET", "params": [{"description": "Chess.com tournament URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}, {"description": "Source round number", "in": "path", "name": "round", "required": true, "type": "integer"}], "path": "/chesscom/tournament/{slug}/{round}", "pathParams": ["slug", "round"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-tournament-round-group": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-tournament-round-group", "method": "GET", "params": [{"description": "Chess.com tournament URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}, {"description": "Source round number", "in": "path", "name": "round", "required": true, "type": "integer"}, {"description": "Source group number", "in": "path", "name": "group", "required": true, "type": "integer"}], "path": "/chesscom/tournament/{slug}/{round}/{group}", "pathParams": ["slug", "round", "group"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["chesscom-club", "chesscom-club-matches", "chesscom-club-members", "chesscom-country", "chesscom-match", "chesscom-match-board", "chesscom-match-live", "chesscom-match-live-board", "chesscom-player", "chesscom-player-clubs", "chesscom-player-game-archives", "chesscom-player-game-month", "chesscom-player-game-month-pgn", "chesscom-player-games", "chesscom-player-games-to-move", "chesscom-player-is-online", "chesscom-player-live-games", "chesscom-player-live-games-base-time", "chesscom-player-matches", "chesscom-player-stats", "chesscom-player-tournaments", "chesscom-puzzle", "chesscom-puzzle-random", "chesscom-tournament", "chesscom-tournament-round", "chesscom-tournament-round-group"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-chesscom-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('club') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-club', params, response_type: response_type)
      end
      define_method('club_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-club-matches', params, response_type: response_type)
      end
      define_method('club_members') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-club-members', params, response_type: response_type)
      end
      define_method('country') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-country', params, response_type: response_type)
      end
      define_method('match_live') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-match-live', params, response_type: response_type)
      end
      define_method('match_live_board') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-match-live-board', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-match', params, response_type: response_type)
      end
      define_method('match_board') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-match-board', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player', params, response_type: response_type)
      end
      define_method('player_clubs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-clubs', params, response_type: response_type)
      end
      define_method('player_games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-games', params, response_type: response_type)
      end
      define_method('player_game_month') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-game-month', params, response_type: response_type)
      end
      define_method('player_game_month_pgn') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-game-month-pgn', params, response_type: response_type)
      end
      define_method('player_game_archives') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-game-archives', params, response_type: response_type)
      end
      define_method('player_live_games_base_time') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-live-games-base-time', params, response_type: response_type)
      end
      define_method('player_live_games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-live-games', params, response_type: response_type)
      end
      define_method('player_games_to_move') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-games-to-move', params, response_type: response_type)
      end
      define_method('player_is_online') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-is-online', params, response_type: response_type)
      end
      define_method('player_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-matches', params, response_type: response_type)
      end
      define_method('player_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-stats', params, response_type: response_type)
      end
      define_method('player_tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-player-tournaments', params, response_type: response_type)
      end
      define_method('puzzle') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-puzzle', params, response_type: response_type)
      end
      define_method('puzzle_random') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-puzzle-random', params, response_type: response_type)
      end
      define_method('tournament') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-tournament', params, response_type: response_type)
      end
      define_method('tournament_round') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-tournament-round', params, response_type: response_type)
      end
      define_method('tournament_round_group') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('chesscom-tournament-round-group', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
