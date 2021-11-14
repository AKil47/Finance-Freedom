<script>
	import Signals from "./Signals.svelte";
	import Graph from "./Graph.svelte";

	export let name;

	let results = {}
	let signals = []
	let signal_weights = []
	let saved_stocks;
	if (localStorage.getItem("saved_stocks") == null) {
		saved_stocks = []
	} else {
		saved_stocks = JSON.parse(localStorage.getItem("saved_stocks"))
	}

	function removeStock(event) {
		saved_stocks = saved_stocks.filter(i => i != event.srcElement.innerText)
		window.localStorage.setItem("saved_stocks", JSON.stringify(saved_stocks))
	}

	async function getStockScore(stock, signals) {
		if (signals != 0) {
			let ret = []
			for (let i = 0; i < signals.length; i++) {
				ret.push({
					"signal": signals[i],
					"weight": signal_weights[i]
				})
			}
			const res = await fetch(`http://localhost:8000/stock/${stock}`, {
				"method": "POST",
				"headers": {
					"Content-Type": "application/json"
				},
				"body": JSON.stringify({
					"signals": ret
				})
			})
			results = await res.json()
		}
	}

	function checkStock() {
		stock = stock_input
		getStockScore(stock, signals)
	}

	function addStock() {
		stock = stock_input
		console.log(stock)
		saved_stocks = [...saved_stocks, stock]
		window.localStorage.setItem("saved_stocks", JSON.stringify(saved_stocks))
	}

	function updateSignal(event) {
		signals = event.detail.signals
		signal_weights = event.detail.signal_weights
		console.log("hi")
		console.log(event.detail.signal_weights)
	}

	//Stock Input stores value of textbox but stock stores the locked value
	let stock_input = "AAPL"
	let stock = "AAPL"

</script>

<svelte:head>
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">
</svelte:head>

<main>
	<div class="Signals">
		<Signals on:SignalUpdate = {updateSignal}></Signals>
	</div>
	<div class="Saved-Stocks">
		<h2 id = "stock-title">My Saved Stocks</h2>
		<ul>
			{#each saved_stocks as stock, s}
				<li class="saved-stock" on:click="{removeStock}">{stock}</li>
			{/each}
		</ul>
		<button style="width: 100%;" on:click="{addStock}">Add</button>
	</div>
	<div class = "Graph">
		<h2 class="Graph-Title">Signal Breakdown</h2>
		<div class="Graph-Area">
			<Graph signals = {results["signals"]}></Graph>
		</div>
	</div>
	<div class="Search-Bar">
		<h1 class="Title">Iconomy</h1>
		<div class="Search-Bar-Area">
			<input id="search-bar" bind:value="{stock_input}" placeholder="Stock Ticker">
			<button id="search-button" on:click="{checkStock}">Search</button>
		</div>
	</div>
	<!-- <p>Score: {results["total"]}</p> -->
</main>

<style>

main {
  display: grid;
  height: 100%;
  width: 100%;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(5, 1fr);
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "Signals Search-Bar Search-Bar Search-Bar"
    "Signals Saved-Stocks Graph Graph"
    "Signals Saved-Stocks Graph Graph"
    "Signals Saved-Stocks Graph Graph"
    "Signals Saved-Stocks Graph Graph";
}

ul {
	overflow-y: auto;
	height: 65%;
	list-style-position: inside;
	text-align: center;
}

.Signals { grid-area: Signals; }

.Saved-Stocks { 
	grid-area: Saved-Stocks;
}

.saved-stock {
	font-size: 3em;
	text-align: center;
}
.saved-stock:hover {
	text-decoration: line-through;
	cursor:pointer;
	color: grey;
}
#stock-title {
	font-size: 3em;
	text-decoration: underline;
	margin-left: 40px;
}

.Graph {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "Graph-Title Graph-Title Graph-Title"
    "Graph-Area Graph-Area Graph-Area"
    "Graph-Area Graph-Area Graph-Area";
  grid-area: Graph;
}

.Graph-Title {
	grid-area: Graph-Title;
	font-size: 3em;
	text-align: center;
	text-decoration: underline;
}

.Graph-Area {
	grid-area: Graph-Area;
	width: 100%;
	height: 100%;
}

.Search-Bar {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "Title Search-Bar-Area Search-Bar-Area"
    "Title Search-Bar-Area Search-Bar-Area"
    "Title Search-Bar-Area Search-Bar-Area";
  grid-area: Search-Bar;
}

#search-bar {
	margin: 0;
	width: 50%;
	height: 40%;
	text-align: center;
	font-size: 4em;
	font-weight: 500;
}

#search-button {
	width: 25%;
	height: 40%;
	margin:0;
}

.Title {
	grid-area: Title;
	font-size: 5em;
	margin-left: 90px;
}

.Search-Bar-Area {
	grid-area: Search-Bar-Area;
	align-items: center;
	display: flex;
	margin-left:150px;
}



</style>