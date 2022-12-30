<script>
	export let name;
	let rand = -1;
	function getRand() {
	  fetch("./rand")
		.then(d => d.text())
		.then(d => (rand = d));
	}
	let speakers = "test";
	function getSpeakers() {
	  fetch("./api/speakers")
		.then(d => d.text())
		.then(d => (speakers = d));
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<h1>Your number is {rand}!</h1>
	<h1>Your number is {speakers}!</h1>
	<button on:click={getRand}>Get a random number</button>
	<button on:click={getSpeakers}>Get a random number</button>

	{#each speakers as speaker}
	<h1> {speaker.player_name}</h1>
{/each}

</main>  


<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>