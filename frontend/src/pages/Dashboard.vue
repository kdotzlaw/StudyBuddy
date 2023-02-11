<script setup>
    import Accordion from "../components/Accordion.vue";
    import ClassCards from "../components/ClassCards.vue";
    import Buddy from "../components/Buddy.vue";
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { userId } = storeToRefs(store);
    const { updateSkin } = store;

    // Stubbed requirements for now
    let reqs = [
        { name: "COMP2080", timeStudied: 2.5 },
        { name: "COMP4350", timeStudied: 6.2 },
        { name: "COMP4620", timeStudied: 0.0 },
        { name: "COMP4380", timeStudied: 10.0 },
    ]
</script>

<template>
    <div id="dashboard">
        <div v-if="userId" id="buddy-ctr">
            <Buddy :showLevel=true chat="Buddy's body is being produced" />
        </div>
        <div v-else id="buddy-ctr">
            <Buddy chat="Ples log in" />
        </div>
        <div v-if="userId">
            <Accordion title="Calendar Overview" :toggled="false">
                <h3>Current Quests</h3>
                <p class="delius">You have an assignment due tomorrow for COMP2080!</p>
            </Accordion>
            <Accordion title="Choose a Class to Study for">
                <ClassCards :reqs="reqs" />
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

    #buddy-ctr{
        position: relative;
        height: 70vh;
        width: 40vw;
        margin-top: 5vh;
        display: grid;
        justify-items: center;
    }
</style>