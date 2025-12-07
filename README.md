# Bitcoin Node Crawler and Heatmap

A Python-based Bitcoin network crawler that discovers Bitcoin **Mainnet** nodes, collects their information, and visualizes them on an interactive world map heatmap. This project connects to the Bitcoin Mainnet network using the official Bitcoin P2P protocol.

## Project Structure

```
Blockchain-Project/
├── backend/           # Python backend code
│   ├── bitcoin_protocol.py    # Bitcoin P2P protocol implementation
│   ├── crawler.py              # Node crawler with asyncio
│   ├── database.py             # SQLite database operations
│   ├── geolocation.py          # IP geolocation services
│   ├── visualization.py        # Heatmap generation
│   ├── main.py                 # Main crawler script
│   ├── create_index.py         # Index page generator
│   ├── update_json.py          # JSON updater
│   └── bitcoin_nodes.db        # SQLite database
├── frontend/          # Frontend files
│   ├── index.html              # Main visualization page
│   └── bitcoin_nodes.json      # Node data (auto-updated)
├── main.py            # Entry point (runs backend/main.py)
├── create_index.py    # Quick script to regenerate index.html
├── open_index.py      # Update JSON and open index.html
└── requirements.txt   # Python dependencies
```

## Features

- **Bitcoin P2P Protocol Implementation**: Implements Bitcoin protocol messages (VERSION, VERACK, GETADDR, ADDR) from scratch
- **Async Crawling**: Uses asyncio for concurrent connections (500+ nodes simultaneously)
- **IP Geolocation**: Automatically geolocates IP addresses to show nodes on a world map
- **SQLite Database**: Stores all node data locally for analysis
- **Interactive Heatmap**: Creates beautiful interactive heatmaps using Folium
- **Statistics**: Generates statistics and visualizations about the Bitcoin network

## How It Works

1. **Protocol Implementation**: The crawler implements Bitcoin's P2P protocol from scratch for **Mainnet**:
   - Connects to Bitcoin Mainnet using magic bytes 0xD9B4BEF9
   - Creates VERSION messages with proper magic bytes and encoding
   - Implements varint encoding/decoding
   - Handles VERSION/VERACK handshake
   - Sends GETADDR and parses ADDR responses to discover peers

2. **Crawling**: 
   - Starts with known Bitcoin Mainnet seed nodes (port 8333)
   - Connects to Mainnet nodes using asyncio for high concurrency
   - Performs Bitcoin Mainnet handshake with each node
   - Requests peer lists (GETADDR) to discover more Mainnet nodes
   - Filters out private IP addresses

3. **Geolocation**:
   - Uses ip-api.com (free tier) to get geographic coordinates
   - Rate-limited to respect API limits

4. **Visualization**:
   - Creates interactive heatmaps showing node density
   - Uses Folium for map rendering
   - Shows statistics overlay

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

### Option 1: Run Live Map (Recommended)

Start the live map with automatic updates. This will:
- Start an HTTP server on `http://localhost:8000`
- Continuously crawl Bitcoin Mainnet nodes every 10 seconds
- Automatically update the visualization
- Open the map in your browser

**From the project root directory:**
```bash
python start_live_map.py
```

The map will automatically refresh every 10 seconds with new node data. Press `Ctrl+C` to stop.

### Option 2: One-Time Crawl and Visualization

Crawl Bitcoin Mainnet nodes once and create a static heatmap:

**From the project root directory:**
```bash
python main.py --max-nodes 1000 --create-heatmap
```

This will:
1. Connect to Bitcoin Mainnet seed nodes
2. Crawl up to 1000 nodes
3. Get geolocation data for each node
4. Store data in the database
5. Generate an interactive heatmap

### Option 3: Run from Backend Directory

You can also run the crawler directly from the `backend` directory:

```bash
cd backend
python main.py --max-nodes 1000 --create-heatmap
```

### Option 4: View Existing Data

If you already have node data in the database, you can generate a heatmap without crawling:

```bash
python main.py --heatmap-only
```

Or regenerate the index page:

```bash
python create_index.py
```

### Option 5: Start HTTP Server Only

To serve the frontend files without auto-updates:

```bash
cd backend
python serve.py
```

Then open `http://localhost:8000/index.html` in your browser.

## Project Structure

```
Blockchain-Project/
├── backend/           # Python backend code
│   ├── bitcoin_protocol.py    # Bitcoin P2P protocol implementation
│   ├── crawler.py              # Node crawler with asyncio
│   ├── database.py             # SQLite database operations
│   ├── geolocation.py          # IP geolocation services
│   ├── visualization.py        # Heatmap generation
│   ├── main.py                 # Main crawler script
│   ├── create_index.py         # Index page generator
│   ├── update_json.py          # JSON updater
│   └── bitcoin_nodes.db        # SQLite database
├── frontend/          # Frontend files
│   ├── index.html              # Main visualization page
│   └── bitcoin_nodes.json      # Node data (auto-updated)
├── main.py            # Entry point (runs backend/main.py)
├── create_index.py    # Quick script to regenerate index.html
├── open_index.py      # Update JSON and open index.html
└── requirements.txt   # Python dependencies
```

## Usage Examples

### Basic Crawling

Crawl 1000 Bitcoin Mainnet nodes and create a heatmap:
```bash
python main.py --max-nodes 1000 --create-heatmap
```

### Advanced Options

```bash
# Crawl with custom settings
python main.py --max-nodes 2000 --max-concurrent 300 --timeout 15.0

# Skip geolocation (faster, but no map)
python main.py --max-nodes 1000 --no-geolocation

# Only create heatmap from existing database
python main.py --heatmap-only

# Custom database path
python main.py --db-path my_nodes.db --create-heatmap
```

### Command Line Arguments

- `--max-nodes`: Maximum number of nodes to crawl (default: 1000)
- `--max-concurrent`: Maximum concurrent connections (default: 500)
- `--timeout`: Connection timeout in seconds (default: 10.0)
- `--no-geolocation`: Skip IP geolocation step
- `--geolocation-rate-limit`: Rate limit for geolocation API (default: 0.15 seconds)
- `--create-heatmap`: Create heatmap visualization after crawling
- `--heatmap-only`: Only create heatmap from existing database
- `--db-path`: Path to SQLite database (default: bitcoin_nodes.db)
- `--output-dir`: Output directory for visualizations (default: current directory)

## Output Files

- `bitcoin_nodes.db`: SQLite database with all node data
- `bitcoin_nodes_heatmap.html`: Interactive world map heatmap
- `bitcoin_nodes_stats.html`: Statistics and charts (if plotly is available)

## Database Schema

The SQLite database contains a `nodes` table with the following fields:
- `ip`: IP address
- `port`: Port number
- `version`: Bitcoin protocol version
- `services`: Services supported
- `user_agent`: Node user agent string
- `timestamp`: When the node was crawled
- `peers_discovered`: Number of peers discovered from this node
- `latitude`, `longitude`: Geographic coordinates
- `country`, `city`: Location information

## Technical Details

### Bitcoin Protocol Implementation

The crawler implements the Bitcoin P2P protocol from scratch and connects to **Bitcoin Mainnet**:

- **Network**: Connects to Bitcoin Mainnet (not testnet or regtest)
- **Magic Bytes**: Uses Bitcoin Mainnet magic bytes (0xD9B4BEF9)
- **Port**: Connects to standard Bitcoin Mainnet port 8333
- **Message Format**: Properly formats messages with magic, command, length, checksum, and payload
- **Varint Encoding**: Implements variable-length integer encoding as per Bitcoin protocol
- **VERSION Message**: Creates proper VERSION messages with all required fields
- **ADDR Parsing**: Parses ADDR messages to extract peer information

### Concurrency

Uses Python's asyncio for high-performance concurrent connections:
- Semaphore-based rate limiting
- Async/await for non-blocking I/O
- Handles 500+ concurrent connections efficiently

### Rate Limiting

- Geolocation API calls are rate-limited to respect free tier limits
- Configurable rate limits via command-line arguments

## Limitations

- **Geolocation API**: Uses free tier of ip-api.com (45 requests/minute limit)
- **IPv6**: Currently focuses on IPv4 addresses
- **Network Size**: Bitcoin network has ~10,000+ nodes; crawling all takes time

## Example Output

After running the crawler, you'll get:
- A database with node information
- An interactive HTML heatmap showing node distribution worldwide
- Statistics about the Bitcoin network

Open `bitcoin_nodes_heatmap.html` in a web browser to see the visualization!

## Troubleshooting

**No nodes crawled**: 
- Check your internet connection
- Try increasing `--timeout`
- Verify seed nodes are accessible

**Geolocation fails**:
- Free API has rate limits; increase `--geolocation-rate-limit`
- Some IPs may not have geolocation data available

**Memory issues**:
- Reduce `--max-concurrent` if running out of memory
- Process in smaller batches

## License

This project is for educational purposes. Use responsibly and respect Bitcoin network resources.

## Credits

Inspired by the work of Ruzanna Hunanyan's team, who implemented Bitcoin P2P handshakes from scratch in Python.

