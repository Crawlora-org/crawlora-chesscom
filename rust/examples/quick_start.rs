use crawlora_chesscom::{serde_json, ChesscomPuzzleParams, Client};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.chesscom.puzzle(Default::default()).await?;
    let data: serde_json::Value = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
