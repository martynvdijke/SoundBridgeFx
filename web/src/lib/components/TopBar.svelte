<script lang="ts">
    import TopAppBar, {
        Row,
        Section,
        Title,
        AutoAdjust,
    } from '@smui/top-app-bar';
    import IconButton from '@smui/icon-button'
    import {Icon, Svg} from '@smui/common';
    import {mdiBrightness6, mdiCog, mdiRefresh, mdiGithub} from '@mdi/js';
    import Drawer, {
        Content,
    } from '@smui/drawer';
    import List, {Item, Text, Graphic} from '@smui/list';

    let lightTheme =
        typeof window === 'undefined' || window.matchMedia('(prefers-color-scheme: light)').matches;

    function switchTheme() {
        lightTheme = !lightTheme;
        let themeLink = document.head.querySelector<HTMLLinkElement>('#theme');
        if (!themeLink) {
            themeLink = document.createElement('link');
            themeLink.rel = 'stylesheet';
            themeLink.id = 'theme';
        }
        themeLink.href = `/smui${lightTheme ? '' : '-dark'}.css`;
        document.head
            .querySelector<HTMLLinkElement>('link[href$="/smui-dark.css"]')
            ?.insertAdjacentElement('afterend', themeLink);
    }
    function refresh(){

    }
    function settings(){

    }
    export let topAppBar: TopAppBar;
    let open = false;
    let active = 'Home';

    function setActive(value: string) {
        active = value;
    }
</script>


<TopAppBar bind:this={topAppBar} class="top-app-bar-container" ariant="standard">
    <Row>
        <Section>
            <IconButton class="material-icons" on:click={() => (open = !open)}>menu</IconButton>
            <Title>SoundbridgeFx</Title>
        </Section>

        <Section align="end" toolbar>
            <IconButton on:click={switchTheme}>
                <Icon component={Svg} viewBox="0 0 24 24">
                    <path fill="currentColor" d={mdiBrightness6}/>
                </Icon>
            </IconButton>
            <IconButton on:click={refresh}>
                <Icon component={Svg} viewBox="0 0 24 24">
                    <path fill="currentColor" d={mdiRefresh}/>
                </Icon>
            </IconButton>
            <IconButton aria-label="GitHub" target="_blank" href="https://github.com/martynvdijke/SoundBridgeFx">
                <Icon component={Svg} viewBox="0 0 24 24">
                    <path fill="currentColor" d={mdiGithub}/>
                </Icon>
            </IconButton>
        </Section>
    </Row>
</TopAppBar>
<div class="drawer-container">
    <Drawer variant="modal" bind:open>
        <Content>
            <List>
                <Item
                        href="http://localhost:6207/"
                        on:click={() => setActive('Home')}
                        activated={active === 'Home'}
                >
                    <Graphic class="material-icons" aria-hidden="true">home</Graphic>
                    <Text>Home</Text>
                </Item>
                <Item
                        href="/ledfx"
                        on:click={() => setActive('LedFx')}
                        activated={active === 'LedFx'}
                >
                    <Graphic class="material-icons" aria-hidden="true">wb_incandescent</Graphic>
                    <Text>LedFX</Text>
                </Item>
                <Item
                        href="/stream"
                        on:click={() => setActive('Stream')}
                        activated={active === 'Stream'}
                >
                    <Graphic class="material-icons" aria-hidden="true">volume_up</Graphic>
                    <Text>Stream</Text>
                </Item>
                <Item   
                href="/settings"
                on:click={() => setActive('Settings')}
                activated={active === 'Settings'}>
                    <Graphic class="material-icons" aria-hidden="true">settings</Graphic>
                    <Text>Settings</Text>
                </Item>
            </List>
        </Content>
    </Drawer>
</div>
<AutoAdjust {topAppBar}>
    <div class="container">
        <slot></slot>
    </div>
</AutoAdjust>

<style>

    .top-app-bar-container {
        width: 100%;
        margin: 0 18px 18px 0;
        overflow: auto;
        display: inline-block;
        position: relative;
    }
    
    .drawer-container {
        position: absolute;
        margin-top: 64px;
        display: flex;
        overflow: hidden;
        z-index: 1;
        top : 0;
        left: 0;
    }

</style>

