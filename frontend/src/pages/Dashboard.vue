<script setup>
    import Accordion from "../components/Accordion.vue";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { updateSkin, setStudyClass } = store;
</script>

<template>
    <div id="dashboard">
        <div>
            Buddy's body is being produced. <br/>
            Buddy will go here soon! <br/>
            <slot />
        </div>
        <div>
            <Accordion title="Calendar Overview" :toggled="false">
                <h3>Current Quests</h3>
                <p class="delius">You have an assignment due tomorrow for COMP2080!</p>
            </Accordion>
            <Accordion title="Choose a Class to Study for">
                <div class="skins">
                    <div :class="`skin-preview skin-default`" @click="setStudyClass('COMP2080')">
                        COMP2080
                    </div>
                    <div :class="`skin-preview skin-forest`" @click="setStudyClass('COMP4350')">
                        COMP4350
                    </div>
                    <div :class="`skin-preview skin-sunset`" @click="setStudyClass('COMP4620')">
                        COMP4620
                    </div>
                </div>
            </Accordion>
            <Accordion title="Choose a UI Skin">
                <div class="skins">
                    <div :class="`skin-preview skin-default`" @click="updateSkin('skin-default')" />
                    <div :class="`skin-preview skin-forest`" @click="updateSkin('skin-forest')" />
                    <div :class="`skin-preview skin-sunset`" @click="updateSkin('skin-sunset')" />
                </div>
            </Accordion>
        </div>
    </div>
</template>

<style scoped>
    #dashboard{
        width: 95%;
        display: flex;
        justify-content: space-between;
        margin: 5vh 0 10vh 0;
    }

    .skins{
        display: flex;
        margin: 1em 0 1em 0;
    }

    .skin-preview{
        height: 4em;
        width: 6em;
        margin: 0 0.5em 0 0.5em;
        border: 2px solid var(--gold);
        border-radius: 0.5em;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        cursor: pointer;
    }

    .skin-preview:hover{
        transition: 0.3s;
        filter: brightness(110%) opacity(80%);
    }
</style>