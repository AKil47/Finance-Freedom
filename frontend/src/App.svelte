<script>
	import Signals from "./Signals.svelte";
	import Graph from "./Graph.svelte";

	export let name;

	let results = {}
	let signals = []
	let saved_stocks;
	if (localStorage.getItem("saved_stocks") == null) {
		saved_stocks = []
	} else {
		saved_stocks = JSON.parse(localStorage.getItem("saved_stocks"))
	}

	async function getStockScore(stock, signals) {
		if (signals != 0) {
			const res = await fetch(`http://localhost:8000/stock/${stock}`, {
				"method": "POST",
				"headers": {
					"Content-Type": "application/json"
				},
				"body": JSON.stringify({
					"signals": signals
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
	}

	//Stock Input stores value of textbox but stock stores the locked value
	let stock_input = "AAPL"
	let stock = "AAPL"

</script>

<main>
	<p>Hello {name}</p>
	<Signals on:SignalUpdate = {updateSignal}></Signals>
	<input bind:value="{stock_input}">
	<button on:click="{checkStock}">Check</button>
	<button on:click="{addStock}">Add</button>
	<Graph signals = {results["signals"]}></Graph>
	<br>
	<p>Saved Stocks</p>
		{#each saved_stocks as stock, s}
			<p>{stock}</p>
		{/each}
</main>

<style>

</style>