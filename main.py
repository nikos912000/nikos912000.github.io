import ltk

width = ltk.window.innerWidth
height = ltk.window.innerHeight


class Main(ltk.Widget):
    def __init__(self, *items):
        ltk.Widget.__init__(
            self,
            *items
        )
        self.width(min(1500, width)).height(850).attr("id", "main").css("margin", "auto")


class Item(ltk.Widget):
    count = 0
    classes = [ "item" ]
    def __init__(self, x, y, width, title, label, src, url):
        ltk.Widget.__init__(
            self,
            ltk.Link(
                url,
                ltk.VBox(
                    ltk.Text(title).css("text-align", "center")
                        .css("font-size", 18)
                        .css("margin-bottom", -2),
                    ltk.Image(src)
                        .css("border", "5px solid transparent")
                        .on("mouseenter", ltk.proxy(
                            lambda e: ltk.find(e.target).css("border-color", "orange")
                        ))
                        .on("mouseleave", ltk.proxy(
                            lambda e: ltk.find(e.target).css("border-color", "transparent")
                        )),
                    ltk.Text(label).css("text-align", "center")
                        .css("font-size", 16)
                ),
            )
            .attr("id", f"item-{Item.count}")
            .attr("target", "_blank")
            .css("position", "absolute")
            .css("text-decoration", "none")
            .css("left", (80 + x))
            .css("top", (40 + y))
            .css("width", width)
            .css("opacity", 0)
            .addClass("item")
        )
        Item.count += 1

items = [
    Item(
        0,
        0,
        200,
        "",
        "Nikos Katirtzis",
        "img/nikos.jpg",
        "https://nikos912000.github.io/",
    ),
    Item(
        0,
        550,
        100,
        "2012",
        "CFG->CNF Converter",
        "img/cfg_cnf_converter.png",
        "https://github.com/nikos912000/chomsky-normal-form",
    ),
    Item(
        100,
        400,
        100,
        "2013",
        "Octree Partitioning",
        "img/octree_partitioning.png",
        "https://github.com/nikos912000/octree-partitioning",
    ),
    Item(
        200,
        530,
        100,
        "2013",
        "Parallel KMeans (MPI)",
        "img/parallel_kmeans.png",
        "https://github.com/nikos912000/kmeans-mpi",
    ),
    Item(
        300,
        400,
        100,
        "2014",
        "Parallel kNN (CUDA)",
        "img/parallel_knn.png",
        "https://github.com/nikos912000/knn-cuda",
    ),
    Item(
        410,
        515,
        100,
        "2014",
        "Parallel Pagerank (Pthreads)",
        "img/parallel_pagerank.png",
        "https://github.com/nikos912000/parallel-pagerank",
    ),
    Item(
        530,
        460,
        100,
        "2014",
        "MEng",
        "img/meng_thesis.png",
        "http://ikee.lib.auth.gr/record/291762/files/katirtzis_nikolaos_tdd_reuse.pdf",
    ),
    Item(
        640,
        430,
        100,
        "2016",
        "MSc",
        "img/msc_thesis.png",
        "https://www.dropbox.com/s/m8uaxa967o3khtp/report.pdf",
    ),
    Item(
        700,
        250,
        100,
        "2017",
        "CLAMS",
        "img/clams.png",
        "https://mast-group.github.io/clams/",
    ),
    Item(
        800,
        400,
        100,
        "2018",
        "FASE",
        "img/clams_fase.png",
        "https://link.springer.com/chapter/10.1007/978-3-319-89363-1_11",
    ),
    Item(
        880,
        200,
        100,
        "2018",
        "Developer Tools",
        "img/hotels.png",
        "https://medium.com/hotels-com-technology/going-beyond-grep-for-searching-source-code-zoekt-e7da88ac7b2e",
    ),
    Item(
        960,
        500,
        100,
        "2019",
        "Java & Performance",
        "img/hotels.png",
        "https://grpc.io/docs/languages/java/#dev-stories",
    ),
    Item(
        1030,
        350,
        100,
        "2020",
        "Mittens",
        "img/mittens.png",
        "https://medium.com/expedia-group-tech/mittens-warming-up-your-application-f8dd244357b0",
    ),
    Item(
        1100,
        150,
        100,
        "2020",
        "Observability",
        "img/expedia_group.png",
        "https://medium.com/expedia-group-tech/creating-monitoring-dashboards-1f3fbe0ae1ac",
    ),
    Item(
        1170,
        500,
        100,
        "2021",
        "Cloud & Reliability Engineering",
        "img/expedia_group_reliability_engineering.png",
        "https://medium.com/expedia-group-tech/using-fault-injection-to-improve-our-new-platforms-reliability-656b1147b132",
    ),
    Item(
        1250,
        100,
        100,
        "2022",
        "Open Source",
        "img/expedia_group_open_source.png",
        "https://medium.com/expedia-group-tech/open-source-at-expedia-group-behind-the-scenes-ecc7d4480566",
    ),
    Item(
        1320,
        350,
        100,
        "2022",
        "Platform Engineering",
        "img/expedia_group.png",
        "https://medium.com/expedia-group-tech/chaos-engineering-at-expedia-group-e51a0288ee2",
    ),
    Item(
        1420,
        200,
        100,
        "2023",
        "Reliability Engineering",
        "img/expedia_group_reliability_engineering.png",
        "https://www.youtube.com/watch?v=CAq2HPNxVcs",
    ),
    Item(
        1500,
        500,
        100,
        "2024",
        "Go & Kubernetes",
        "img/expedia_group.png",
        "https://www.infoq.com/news/2024/04/expedia-startup-autoscaler/",
    ),
    Item(
        1570,
        250,
        100,
        "2024",
        "Randomly Learning",
        "img/randomly_learning.png",
        "https://github.com/nikos912000/randomly-learning/",
    ),
    Item(
        1650,
        500,
        100,
        "2024",
        "Data Engineering",
        "img/slo_platform.png",
        "https://medium.com/expedia-group-tech/enhancing-data-reliability-with-an-slo-platform-de00249756f6",
    ),
]

def tile(url, image, label, width=120, height=120):
    return ltk.Link(url,
        ltk.VBox(
            #todo make it work with https://nikos912000.github.io
            ltk.Image(f"/img/{image}")
                .css("border", "5px solid transparent")
                .on("mouseenter", ltk.proxy(
                    lambda e: ltk.find(e.target).css("border-color", "orange")
                ))
                .on("mouseleave", ltk.proxy(
                    lambda e: ltk.find(e.target).css("border-color", "transparent")
                ))
                .css("width", width)
                .css("height", height),
            ltk.Text(label).css("font-size", 16)
        )
        .css("float", "left")
        .css("width", 120)
        .css("margin", 25)
        .css("align-items", "center")
        .css("text-align", "center")
    ).attr("target", "_blank")

tiles = [
    tile("https://github.com/nikos912000/randomly-learning/", "randomly_learning.png", "Randomly Learning"),
    tile("https://opensource.datadoghq.com/projects/chaos-controller/#external-contributions-spotlight", "chaos_controller.png", "Chaos Controller"),
    tile("https://github.com/ExpediaGroup/mittens", "mittens_square.png", "Mittens"),
    tile("https://github.com/HotelsDotCom/hapidoc-web", "hapidoc.png", "HApiDoc"),
    tile("https://mast-group.github.io/clams/", "clams.png", "CLAMS"),
    tile("http://mantissa.ee.auth.gr:5050/", "mantissa.png", "Mantissa"),
    tile("https://github.com/nikos912000", "github.png", "GitHub"),
    tile("https://medium.com/@nkatirtzis/list/contributions-6ca764e7fe66", "medium.png", "Medium"),
    tile("https://substack.com/@nikoskatirtzis", "substack.png", "Substack"),
    tile("https://www.linkedin.com/in/nkatirtzis/", "linkedin.png", "LinkedIn"),
    tile("https://mastodon.social/@nikos912000", "mastodon.png", "Mastodon"),
    tile("https://twitter.com/nikos912000/", "twitter.png", "Twitter"),
    tile("https://bsky.app/profile/nikos912000.bsky.social", "bluesky.png", "Bluesky"),
    tile("https://scholar.google.com/citations?hl=en&user=97v69QoAAAAJ", "google_scholar.png", "Publications"),
    tile("https://speakerdeck.com/nikos912000", "speakerdeck.png", "Slides"),
    tile("https://youtube.com/playlist?list=PL91tHEodCy_GwWJKbqaB-aFQ_jXOa7442&si=oO7h8E4hBQKQGOpZ", "youtube.png", "Youtube"),
]

(
    ltk.VBox(
        ltk.Heading1("Nikos Katirtzis").css("font-size", 32).css("text-align", "center"),
        Main(*items).css("position", "relative")
            .css("margin-bottom", 50),
        ltk.VBox(
            ltk.Heading2("For more details select any item shown in the visual resume above or in the list below")
                .css("width", min(400, width - 250))
                .css("color", "gray")
                .css("margin-right", 100)
                .css("text-align", "center"),
            ltk.Div(*tiles)
                .attr("id", "tiles")
        )
        .css("width", min(800, width - 50))
        .css("margin-left", width * 0.1)
        .css("align-items", "center")
        .css("margin", "auto")
        .attr("id", "rest")
        .css("opacity", 0)
    )
    .css("width", "100%")
    .css("margin", "auto")
    .appendTo(ltk.window.document.body)
)

items = ltk.find_list(".item .ltk-a")

def get_line(n):
    start = items[n]
    end = items[n+1]
    x1 = ltk.parse_float(start.css("left")) + start.width() / 2
    y1 = ltk.parse_float(start.css("top")) + start.height() / 2
    x2 = ltk.parse_float(end.css("left")) + end.width() / 2
    y2 = ltk.parse_float(end.css("top")) + end.height() / 2
    return f'<line id="line-{n}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:white;stroke-dasharray:5,5;stroke-width:2" />'

ltk.find("#main").append(
    ltk.create(f"""
        <svg id="svg" height="850" width="2000">
            <line x1="40" y1="20" x2="40" y2="800" style="stroke:lightgray;stroke-width:2" />
            <line x1="0" y1="770" x2="2000" y2="770" style="stroke:lightgray;stroke-width:2" />

            <text x="200" y="807" style="font-size:16pt; fill:gray">noob</text>
            <text x="1800" y="807" style="font-size:16pt; fill:gray">now</text>
            <text x="1035" y="807" style="font-size:16pt; fill:lightgray">time</text>

            <line x1="900" y1="800" x2="1000" y2="800" style="stroke:lightgray;stroke-width:2" />
            <line x1="1200" y1="800" x2="1180" y2="790" style="stroke:lightgray;stroke-width:2" />
            <line x1="1200" y1="800" x2="1180" y2="810" style="stroke:lightgray;stroke-width:2" />

            <line x1="1100" y1="800" x2="1200" y2="800" style="stroke:lightgray;stroke-width:2" />
            <line x1="900" y1="800" x2="920" y2="790" style="stroke:lightgray;stroke-width:2" />
            <line x1="900" y1="800" x2="920" y2="810" style="stroke:lightgray;stroke-width:2" />

            <text style="font-size:16pt; fill:gray;" transform="translate(28,85) rotate(270)">Human</text>
            <text style="font-size:16pt; fill:gray;" transform="translate(28,685) rotate(270)">Technical</text>
            <text style="font-size:16pt; fill:lightgray;" transform="translate(28,385) rotate(270)">focus</text>

            <line x1="20" y1="200" x2="20" y2="300" style="stroke:lightgray;stroke-width:2" />
            <line x1="10" y1="220" x2="20" y2="200" style="stroke:lightgray;stroke-width:2" />
            <line x1="30" y1="220" x2="20" y2="200" style="stroke:lightgray;stroke-width:2" />

            <line x1="20" y1="420" x2="20" y2="520" style="stroke:lightgray;stroke-width:2" />
            <line x1="10" y1="500" x2="20" y2="520" style="stroke:lightgray;stroke-width:2" />
            <line x1="30" y1="500" x2="20" y2="520" style="stroke:lightgray;stroke-width:2" />

            { "".join([get_line(n) for n in range(1, len(items) - 1)]) }
        </svg>
    """).css("margin", "auto")
)

def show(index):
    ltk.find(f"#line-{index - 1}").css("stroke", "pink")
    item = ltk.find(f"#item-{index}")
    body = ltk.find("html, body")
    if not item.length:
        ltk.find("#rest").animate(ltk.to_js({ "opacity": 1 }), 1000)
        body.animate(ltk.to_js({ "scrollTop": height - 800 }), 1500, 'swing', lambda:
            body.animate(ltk.to_js({ "scrollTop": 0 }), 300, 'swing')
        )
        return
    x = ltk.parse_float(item.css("left"))
    y = ltk.parse_float(item.css("top"))
    w = item.width()
    h = item.height()
    item.css(ltk.to_js({
        "left": x + w / 2,
        "top": y + h / 2,
        "width": 0,
        "height": 0,
    })).animate(
        ltk.to_js({
            "top": y,
            "left": x,
            "width": w,
            "height": h,
            "opacity": 1,
        }),
        50,
        lambda: show(index + 1)
    )
    if x > width - 200:
        ltk.find("#main").animate(
            ltk.to_js({
                "left": -x + width * 3 /4,
            }), 1000,
            lambda: ltk.find("#main").animate(
                ltk.to_js({
                    "left": 0,
                }), 1000
            )
        )

show(0)
