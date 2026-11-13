require_relative "lib/crawlora/chesscom/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-chesscom"
  spec.version = Crawlora::Chesscom::VERSION
  spec.summary = "Chess.com API client for Crawlora (26 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Chess.com API. Covers puzzles, player and club resources, tournaments, and public team matches across 26 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-chesscom", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-chesscom/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
