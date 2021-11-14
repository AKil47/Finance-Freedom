<script>
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    let signals = []
    let signals_checked = []
    let signals_score = []
    let checked_signals = []
    let checked_signals_scores = []

    onMount(async () => {
		const res = await fetch("http://localhost:8000/signal", {
        "method": "GET",
        "headers": {}
            });
		signals = await res.json();
        for (let i = 0; i < signals.length; i++) {
            signals_checked[i] = false
            signals_score[i] = 5
        }
	});

    //Send checked boxes to API whenever they change
    $: {
        checked_signals = []
        checked_signals_scores = []
        for (let i = 0; i < signals_checked.length; i++) {
            if (signals_checked[i]) {
                checked_signals.push(signals[i])
                checked_signals_scores.push(signals_score[i])
            }
        }

        dispatch("SignalUpdate", {
            "signals": checked_signals,
            "signal_weights": checked_signals_scores
        })
    }
</script>

<div>
    {#each signals as signal, index}
    <div class = "signal">
        <label for="{index}">
            <input type="checkbox" id="{index}" value="{index}" bind:checked = {signals_checked[index]}> {signal}
            <input type="range" min = "1" max = "10" bind:value={signals_score[index]}>
            <input type = "number" bind:value="{signals_score[index]}">
        </label>
    </div>
    {/each}
</div>

<style>
    .signal {
        padding: 5%;
    }

    input{
        width: 100%;
    }

    input[type=range] {
        overflow: hidden;
        background-color: #9a905d;
    }
</style>