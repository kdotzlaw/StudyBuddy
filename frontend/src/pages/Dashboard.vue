<!-- 
  Dashboard.vue
    route: /
    Primary homepage and application entrypoint. Conditionally mount dashboard components based on user authentication state. 
-->

<script setup>
    import { default as axios } from 'axios';
    import Accordion from "../components/Accordion.vue";
    import ClassCards from "../components/ClassCards.vue";
    import RequirementCards from "../components/RequirementCards.vue";
    import Buddy from "../components/Buddy.vue";
    import { ref, computed, onMounted } from "vue";
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    import filter from "../logic/filter";
    
    const store = useStore();
    const { userId } = storeToRefs(store);
    const { updateSkin, setPageName } = store;

    let classes = [
        { name: "COMP2080", timeStudied: 2.5 },
        { name: "COMP4350", timeStudied: 6.2 },
        { name: "COMP4620", timeStudied: 0.0 },
        { name: "COMP4380", timeStudied: 10.0 },
    ]
    // Return color tag by class key
    function getTagColor(key) {
        let map = {
            "COMP2080": "red",
            "COMP4350": "blue",
            "COMP4620": "green",
            "COMP4380": "yellow",
        }
        let mapping = map[key];
        if(!mapping)
            return "grey";
        return mapping;
    }
    let reqsFiltered = filter.getReqs([
        { classKey: "COMP4620", tagColor: getTagColor("COMP4620"), name: "Assignment 4", due: new Date("March 12, 2023"), goal: "C" },
        { classKey: "COMP2080", tagColor: getTagColor("COMP2080"), name: "Catch up", due: new Date("March 13, 2023"), goal: "C" },
        { classKey: "COMP4350", tagColor: getTagColor("COMP4350"), name: "Final Exam", due: new Date("April 20, 2023"), goal: "A+" },
    ]);
    let chatsFiltered = filter.getChats([
        { classKey: "COMP4620", tagColor: getTagColor("COMP4620"), name: "Assignment 4", due: new Date("March 12, 2023"), goal: "C" },
        { classKey: "COMP2080", tagColor: getTagColor("COMP2080"), name: "Catch up", due: new Date("March 13, 2023"), goal: "C" },
        { classKey: "COMP4350", tagColor: getTagColor("COMP4350"), name: "Final Exam", due: new Date("April 20, 2023"), goal: "A+" },
    ]);
    const reqs = ref(reqsFiltered);
    const chats = ref(chatsFiltered);

    let chatIndex = 0;
    const chat = ref(chats.value[0]);
    
    // Cycle through Buddy chat balloon conversations
    setInterval(()=>{
        chatIndex = (chatIndex + 1) % chats.value.length;
        chat.value = chats.value[chatIndex];
    },4000)

    onMounted(() => {
        setPageName("Dashboard");
        if(userId.value)
            getData();  
    })

    const triggerGet = computed(() => {
        if(userId.value){
            getData();
            return 1;
        }
        return 0;
    });

    function getData(){
        // Get classes
        const host = 'http://127.0.0.1:5000'; 
        let apiUrlClass = '/api/class';
        axios.get(host + apiUrlClass)
            .then(function (response) {
                console.log(response);
                
                // Get requirements from classes
                let classList = Object.keys(response.json());
                for (let classKey of classList){
                    const apiUrlTask = `/api/class/${classKey}/task`;
                    axios.get(host + apiUrlTask)
                        .then(function (response) {
                            console.log(response);
                            let tasks = response.json();
                            reqs.value = filter.getReqs(tasks);
                            chats.value = filter.getChats(tasks);
                        })
                        .catch(function (error) {
                            console.log(error.response);
                        })
                }
            })
            .catch(function (error) {
                console.log(error.response);
            })
    }
</script>

<template>
    <div id="dashboard">

        <!-- Buddy container -->
        <div v-if="userId" id="buddy-ctr">
            <Buddy :showLevel=true :chat="chat" />
        </div>
        <div v-else id="buddy-ctr">
            <Buddy chat="Login or Register to use Study Buddy" />
        </div>

        <!-- Dashboard accordions -->
        <div v-if="userId" v-motion-slide-bottom>
            <Accordion title="Calendar Overview" :toggled="false">
                <h3>Current Tasks</h3>
                <RequirementCards :reqs="reqs" :borderless="true" />
            </Accordion>
            <Accordion title="Choose a Class to Study for">
                <ClassCards :reqs="classes" />
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

    @media screen and (max-width: 820px) {
        #dashboard{
            flex-direction: column;
        }

        #buddy-ctr{
            width: 100%;
            transform: translateX(-10%);
        }
    }
</style>