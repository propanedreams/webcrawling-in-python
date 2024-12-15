<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Crawler with SQLite</title>
</head>
<body>
    <header>
        <h1>🕸️ Web Crawler with SQLite Storage</h1>
        <p>A Python-based web crawler that collects data from websites, including their titles, meta descriptions, and H1 tags. The data is stored in an SQLite database for easy retrieval and analysis.</p>
    </header>

    <section>
        <h2>🚀 Features</h2>
        <ul>
            <li>🌐 <b>Web Crawling:</b> Visits and indexes web pages starting from a specified base URL.</li>
            <li>📊 <b>Data Collection:</b> Extracts and saves:
                <ul>
                    <li>Page URL</li>
                    <li>Title tag content</li>
                    <li>Meta description content</li>
                    <li>H1 tags content</li>
                    <li>Timestamp of the crawl</li>
                </ul>
            </li>
            <li>🤖 <b>Robots.txt Handling:</b> Respects the <code>robots.txt</code> directives of each website.</li>
            <li>🗄️ <b>SQLite Storage:</b> Efficiently stores crawled URLs and metadata in a database.</li>
            <li>📤 <b>Data Export:</b> Option to export stored data to a CSV file.</li>
            <li>⚙️ <b>Configurable Crawl Depth:</b> Limit the number of pages crawled for performance control.</li>
        </ul>
    </section>

    <section>
        <h2>🛠️ Requirements</h2>
        <p>To use this project, you need:</p>
        <ul>
            <li>Python 3.8 or newer</li>
            <li>Libraries:
                <ul>
                    <li><code>requests</code></li>
                    <li><code>beautifulsoup4</code></li>
                    <li><code>sqlite3</code></li>
                </ul>
            </li>
        </ul>
        <p>Install the required libraries using pip:</p>
        <pre><code>pip install requests beautifulsoup4</code></pre>
    </section>

    <section>
        <h2>📖 Usage</h2>

        <h3>🕵️‍♂️ Web Crawler</h3>
        <ol>
            <li>Set the <code>base_url</code> and <code>max_pages</code> parameters in the crawler script.</li>
            <li>Run the crawler:
                <pre><code>python web_crawler.py</code></pre>
            </li>
        </ol>
        <p>The crawler will:</p>
        <ul>
            <li>Respect <code>robots.txt</code> restrictions.</li>
            <li>Extract relevant metadata from each visited page.</li>
            <li>Save the crawled data to an SQLite database (<code>visited_sites.db</code>).</li>
        </ul>

        <h3>📋 Data Viewer and Exporter</h3>
        <ol>
            <li>Run the data display script to view the stored data:
                <pre><code>python display_data.py</code></pre>
            </li>
            <li>Optionally, export the data to a CSV file when prompted.</li>
        </ol>
    </section>

    <section>
        <h2>🗃️ Database Schema</h2>
        <p>The SQLite database (<code>visited_sites.db</code>) is structured as follows:</p>
        <table border="1">
            <thead>
                <tr>
                    <th>Column</th>
                    <th>Type</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>id</code></td>
                    <td>INTEGER</td>
                    <td>Unique identifier for each record.</td>
                </tr>
                <tr>
                    <td><code>url</code></td>
                    <td>TEXT</td>
                    <td>URL of the visited page.</td>
                </tr>
                <tr>
                    <td><code>title</code></td>
                    <td>TEXT</td>
                    <td>Title tag content of the page.</td>
                </tr>
                <tr>
                    <td><code>meta_description</code></td>
                    <td>TEXT</td>
                    <td>Meta description content of the page.</td>
                </tr>
                <tr>
                    <td><code>h1_tags</code></td>
                    <td>TEXT</td>
                    <td>Comma-separated H1 tag contents.</td>
                </tr>
                <tr>
                    <td><code>timestamp</code></td>
                    <td>DATETIME</td>
                    <td>Timestamp of when the page was crawled.</td>
                </tr>
            </tbody>
        </table>
    </section>

    <section>
        <h2>🔍 Example</h2>

        <h3>Crawling</h3>
        <p>Set the <code>base_url</code> in <code>web_crawler.py</code>:</p>
        <pre><code>crawler = WebCrawler(base_url="https://example.com", max_pages=10)
crawler.crawl()</code></pre>

        <h3>Displaying Data</h3>
        <p>Run the display script:</p>
        <pre><code>python display_data.py</code></pre>
        <p>Sample output:</p>
        <pre><code>ID    URL                             Title               Meta Description        H1 Tags           Timestamp
1     https://example.com             Example Title       Example Meta Desc.     Welcome, About    2024-12-10 10:00:00
2     https://anotherexample.com      Another Title       Another Meta Desc.     Contact, Blog     2024-12-10 10:05:00
</code></pre>

        <h3>Exporting Data</h3>
        <p>When prompted, type <code>yes</code> to export the data to <code>visited_sites.csv</code>.</p>
    </section>

    <section>
        <h2>⚠️ Limitations</h2>
        <ul>
            <li>The crawler may be blocked by certain websites due to IP bans or aggressive rate-limiting.</li>
            <li>It does not execute JavaScript, so content rendered dynamically by JavaScript may not be indexed.</li>
            <li>Ensure compliance with the terms of service for the websites you crawl.</li>
        </ul>
    </section>

    <section>
        <h2>🛠️ Future Enhancements</h2>
        <ul>
            <li>🔄 <b>Multi-threading:</b> Add support for parallel crawling.</li>
            <li>📦 <b>Additional Tags:</b> Scrape more structured data, such as Open Graph or JSON-LD.</li>
            <li>🖥️ <b>Front-End Interface:</b> Build a front-end to display and export data.</li>
            <li>🛡️ <b>Proxy Support:</b> Enable crawling with proxies to bypass rate limits or IP bans.</li>
        </ul>
    </section>

    <footer>
        <h2>📜 License</h2>
        <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

        <h2>🙏 Acknowledgments</h2>
        <ul>
            <li><a href="https://www.crummy.com/software/BeautifulSoup/" target="_blank">BeautifulSoup</a> for HTML parsing.</li>
            <li><a href="https://docs.python-requests.org/en/latest/" target="_blank">Requests</a> for making HTTP requests.</li>
            <li><a href="https://www.sqlite.org/" target="_blank">SQLite</a> for lightweight database storage.</li>
        </ul>
    </footer>
</body>
</html>
