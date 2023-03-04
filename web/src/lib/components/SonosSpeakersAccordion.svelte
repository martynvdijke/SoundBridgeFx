<script lang="ts" context="module">
    import Accordion, {Panel, Header, Content} from '@smui-extra/accordion';
    import {onMount} from "svelte";
    import Checkbox from '@smui/checkbox';
    import FormField from '@smui/form-field';

    export let speakers = [];
    export let selected = [];
    let result = null


    onMount(async () => {
        fetch("http://localhost:6207/api/v1/speakers/all")
            .then(response => response.json())
            .then(data => {
                console.log(data);
                speakers = data.all_speakers[0];
                speakers = speakers.sonos_speakers;
                console.log(speakers);
                console.log(Object.values(speakers));
            }).catch(error => {
            console.log(error);
            return [];
        });
    });
</script>

<div class="accordion-container">
    TEstwts
    <Accordion>
        {#each speakers as speaker}
            <FormField>
                <Checkbox bind:group={selected} value={speaker.player_name}/>
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


<style>
    :global(.mdc-form-field) {
        margin: 0.25em;
        padding: 0.25em;
        display: flex;
    }
</style>
