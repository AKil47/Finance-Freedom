<script>
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    let signals = []
    let signals_checked = []
    let checked_signals = []

    onMount(async () => {
		const res = await fetch("http://localhost:8000/signal", {
        "method": "GET",
        "headers": {}
            });
		signals = await res.json();
        for (let i = 0; i < signals.length; i++) {
            signals_checked[i] = false
        }
	});

    //Send checked boxes to API whenever they change
    $: {
        checked_signals = []
        for (let i = 0; i < signals_checked.length; i++) {
            if (signals_checked[i]) {
                checked_signals.push(signals[i])
            }
        }

        dispatch("SignalUpdate", {
            "signals": checked_signals
        })
    }
</script>

<div>
    {#each signals as signal, index}
    <div class = "signal">
        <label for="{index}">
            <input type="checkbox" id="{index}" value="{index}" bind:checked = {signals_checked[index]}> {signal}
        </label>
    </div>
    {/each}
</div>

<style>
    .signal {
        padding: 1px;
    }
</style>