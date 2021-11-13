<script>
    import { onMount } from 'svelte';

    let stocks = []

    onMount(async () => {
		const res = await fetch("http://localhost:8000/signal", {
        "method": "GET",
        "headers": {}
            });
		stocks = await res.json();
	});
</script>

<ul>
    {#each stocks as stock, _}
    <li>{stock}</li>
    {/each}
</ul>

<style>

</style>