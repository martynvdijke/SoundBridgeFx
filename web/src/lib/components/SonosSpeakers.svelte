<script lang="ts">
    import Accordion, {Panel, Header, Content} from '@smui-extra/accordion';
    import Checkbox from '@smui/checkbox';
    import FormField from '@smui/form-field';
    import Button from '@smui/button';
    import LayoutGrid, {Cell} from '@smui/layout-grid';

    export let speakers: any[] = [];
    let selected_speakers: any[] = [];
    let result = null

    async function getSpeakers() {
        const res = await fetch('http://localhost:6207/api/v1/speakers/all')
        const data = await res.json();
        if (res.ok) {
            speakers = data.all_speakers[0];
            speakers = speakers.sonos_speakers;
        } else {
            throw new Error(data)
        }

    }

    let promise = getSpeakers();

    async function playStream() {
        const res = await fetch('http://localhost:6207/api/v1/speakers/play/stream', {
            method: 'POST',
            body: JSON.stringify({
                selected: selected_speakers
            })
        })
        const json = await res.json()
        console.log(json);
        result = JSON.stringify(json)
    }

    async function playParty() {
        const res = await fetch('http://localhost:6207/api/v1/speakers/play/party', {
            method: 'POST',
            body: JSON.stringify({
                selected: selected_speakers
            })
        })
        const json = await res.json()
        console.log(json);
        result = JSON.stringify(json)
    }

</script>

{#await promise}
    <p> Loading speakers</p>
{:then speaker}
    <div class="flex-container">
        <div class="mdc-typography--headline1">Found Sonos Speakers</div>
        <div class="accordion-container">
            <Accordion>
                {#each speakers as speaker}
                    <FormField>
                        <Checkbox bind:group={selected_speakers} value={speaker.player_name}/>
                        <!-- <span slot="label">{speaker.player_name}</span> -->
                        <Panel>
                            <Header>{speaker.player_name}</Header>
                            <Content>
                                Currently playing : {speaker.object.current_transport_info.current_transport_state} <br>
                                Model : {speaker.object.speaker_info.model_name}
                            </Content>
                        </Panel>
                    </FormField>
                {/each}
            </Accordion>
        </div>

        <div style="margin-top: 1em;">
            <pre class="status">Selected speakers: {selected_speakers.join(', ')}</pre>
        </div>

        <LayoutGrid>
            <Cell span={6}>
                <div class="cell">
                    <Button on:click={playStream}>Play stream</Button>
                </div>
            </Cell>
            <Cell span={6}>
                <div class="cell">
                    <Button on:click={playParty}>Play party mode</Button>
                </div>
            </Cell>
        </LayoutGrid>

    </div>

{:catch error}
    <p>Error {error}</p>
{/await}

<style>
    :global(.mdc-form-field) {
        margin: 0.25em;
        padding: 0.25em;
        display: flex;
    }

    .flex-container {
        margin: auto;
        width: 70%;
        padding: 1em;
        justify-content: center;
        align-items: center;
    }

    .cell {
        margin-top: 1em;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
