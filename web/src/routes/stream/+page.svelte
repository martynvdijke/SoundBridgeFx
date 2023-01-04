<script>
    let innerWidth = 0
    let innerHeight = 0
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<div>
	<iframe src="http://localhost:8889/stream.mp3" height={innerHeight - innerHeight/10} width={innerWidth - innerWidth/200} title="stream iframe"></iframe>
</div>