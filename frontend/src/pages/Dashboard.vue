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

    #buddy-ctr{
        position: relative;
        height: 70vh;
        width: 40vw;
        margin-top: 5vh;
        display: grid;
        justify-items: center;
    }
</style>