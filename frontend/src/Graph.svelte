<svelte:head>
    <script type="text/javascript" src="https://rawgit.com/nnnick/Chart.js/2.0.0-alpha3/Chart.js"></script>
</svelte:head>

<script>
import { afterUpdate } from "svelte";


    export let signals = {"stockscore":60,"WSB Sentiment":66}


    window.onload = build

    let firstTime = true;
    afterUpdate(() => {
         if (!firstTime) {
             myDoughnut.destroy()
            build()
        } else {
            firstTime = false;
        }
    })


    function build_datasets() {
        let datasets = []
        for (let signal in signals) {
            datasets.push({
                data: [signals[signal], 100 - signals[signal]],
                backgroundColor: ["#F7464A", "#949FB1" ],
                label: signal
            })
        }

        return datasets
    }

    let myDoughnut;
    let ctx;
    
    function build() {
        let x = build_datasets()
    	var config = {
    		type: 'doughnut',
    		data: {
                datasets: x,
                labels: ["Positive", "Negative"]
    		},
    		options: {
    			responsive: true
    		}
    	};
    	ctx = document.getElementById("chart-area").getContext("2d");
    	myDoughnut = new Chart(ctx, config);
    }
</script>

<canvas id="chart-area" width=9 height=3></canvas>