# Bitcoin Node Crawler and Heatmap

A Python-based Bitcoin network crawler that discovers Bitcoin **Mainnet** nodes, collects their information, and visualizes them on an interactive world map heatmap.

## Features

- **Bitcoin P2P Protocol Implementation**: Implements Bitcoin protocol messages from scratch
- **Async Crawling**: Uses asyncio for concurrent connections (500+ nodes simultaneously)
- **IP Geolocation**: Automatically geolocates IP addresses to show nodes on a world map
- **Interactive Heatmap**: Creates interactive heatmaps showing node distribution worldwide
- **Static Frontend**: Frontend can be deployed as a static website

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Update Node Data

To crawl new Bitcoin nodes and update `frontend/bitcoin_nodes.json`:

```bash
# Step 1: Crawl new nodes and add to database
python3 main.py --max-nodes 1000 --create-heatmap

# Step 2: Update JSON file with ALL nodes from database
python3 -m backend.update_json
```

**Note:** The `--create-heatmap` flag only exports newly crawled nodes. Always run `python3 -m backend.update_json` after crawling to get all nodes in the JSON file.

### 2. Run the Server

Start the HTTP server to view the map:

```bash
python3 start_live_map.py
```

This will:
- Start a server on `http://localhost:8000`
- Open the map in your browser
- Display nodes from `frontend/bitcoin_nodes.json`

Press `Ctrl+C` to stop the server.

**If port 8000 is already in use:**
```bash
lsof -ti :8000 | xargs kill -9
```

## Detailed Usage

### Update Node Data Only

If you only want to update the JSON file from existing database data:

```bash
python3 -m backend.update_json
```

### View Existing Data

If you already have node data in the database and want to create a heatmap:

```bash
python3 main.py --heatmap-only
```

## Deployment

The `frontend/` directory can be deployed as a **static website** to any hosting service (GitHub Pages, Netlify, Vercel, etc.).

**No server-side code is needed** - just upload the `frontend/` folder contents. The map will work as long as all files (`index.html`, `map.js`, `styles.css`, `bitcoin_nodes.json`) are accessible via HTTP/HTTPS.

## Command Line Options

- `--max-nodes`: Maximum number of nodes to crawl (default: 1000)
- `--max-concurrent`: Maximum concurrent connections (default: 500)
- `--timeout`: Connection timeout in seconds (default: 10.0)
- `--no-geolocation`: Skip IP geolocation step
- `--create-heatmap`: Create heatmap visualization after crawling
- `--heatmap-only`: Only create heatmap from existing database

## Troubleshooting

**No nodes crawled**: Check your internet connection or try increasing `--timeout`

**Geolocation fails**: Free API has rate limits; increase `--geolocation-rate-limit`

**JSON file not updating**: Run `python3 -m backend.update_json` to manually update it

## License

This project is for educational purposes. Use responsibly and respect Bitcoin network resources.
