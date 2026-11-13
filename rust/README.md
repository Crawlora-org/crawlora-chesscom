# Crawlora Chess.com Rust SDK

[![Crates.io](https://img.shields.io/crates/v/crawlora-chesscom.svg)](https://crates.io/crates/crawlora-chesscom)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Official async Rust client for Crawlora's hosted Chess.com API. It exposes
typed request parameters and response handling for 26 public
operations. It calls Crawlora's hosted service; it does not scrape Chess.com
locally. Requests use your Crawlora account and follow its billing plan. Crawlora
is independent from and not affiliated with or endorsed by Chess.com or
its owners.

[Crawlora](https://crawlora.net?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-homepage) ·
[API documentation](https://crawlora.net/docs?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-api-docs) ·
[Pricing](https://crawlora.net/pricing?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-pricing) ·
[Create an account](https://crawlora.net/signup?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-signup)

- **Rust:** 1.88 or newer
- **Async runtime:** Tokio
- **Authentication:** Crawlora API key (`x-api-key`)
- **Operations:** [Rust reference](docs/operations.md) · [all endpoints and parameters](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md)

## Install

```sh
cargo add crawlora-chesscom
```

To pin a release directly in `Cargo.toml`:

```toml
[dependencies]
crawlora-chesscom = "0.1.0"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-signup), then [create an API key](https://crawlora.net/app/api-keys?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-api-keys). Keep the key out of source control and load it from the environment:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Quick start

```rust,no_run
use crawlora_chesscom::{Client, ChesscomPuzzleParams, serde_json};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .chesscom
        .puzzle(Default::default())
        .await?;
    let data: serde_json::Value = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
```

Endpoint methods return the complete HTTP response. Use `into_json()` to decode
JSON into `serde_json::Value` or a generated response model. The response also
preserves headers and status; text and byte response modes are available through
`RequestOptions`.

## Configuration and errors

`CrawloraClient::builder()` supports a custom API base URL, timeout, retry limit,
default headers, JWT authentication, and a custom HTTP client. Retry behavior is
bounded and honors `Retry-After`. API failures are returned as `Error::Api` with
the HTTP status, response body, and request ID when provided.

## More resources

- Read the [generated Rust operation reference](docs/operations.md).
- Browse the [complete endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md).
- Review the [hosted API documentation](https://crawlora.net/docs?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-api-docs) and [pricing](https://crawlora.net/pricing?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-rust-pricing).

## License

MIT. See [LICENSE](LICENSE).
