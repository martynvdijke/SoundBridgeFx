<script lang="ts">
	import TopAppBar from '$lib/components/TopBar.svelte'
</script>

<svelte:head>
    <title>SoundBridgeFX</title>
    <meta name="description" content="SoundBridgeFx" />
</svelte:head>

<TopAppBar>
<slot></slot>
</TopAppBar>

<style>
	:global(body) { margin: 0; padding: 0; }
</style>
