require "json"
require "minitest/autorun"
require "crawlora/chesscom"

class PlatformClientTest < Minitest::Test
  def test_operation_allowlist_and_mocked_request
    calls = []
    transport = lambda do |url, headers, timeout|
      calls << [url, headers, timeout]
      { status: 200, headers: { "content-type" => "application/json" }, body: '{"ok":true}' }
    end
    client = Crawlora::Chesscom::Client.new(
      api_key: "test-key",
      base_url: "https://api.example.test/api/v1",
      transport: transport
    )

    result = client.request("chesscom-club", JSON.parse("{\"slug\": \"sample-id\"}"))
    assert_equal({ "ok" => true }, result)
    assert_equal 1, calls.length
    assert_includes calls.first[0], "/chesscom/"
    assert_equal ["test-key"], calls.first[1]["x-api-key"]
    assert_equal 26, Crawlora::Chesscom::Client.operation_count
    default_client = Crawlora::Chesscom::Client.new(api_key: "test-key", transport: transport)
    assert_equal "https://api.crawlora.net/api/v1", default_client.base_url
    assert_raises(Crawlora::Chesscom::Errors::ClientError) do
      client.request("unlisted-operation")
    end
  ensure
    client&.close
    default_client&.close
  end
end
