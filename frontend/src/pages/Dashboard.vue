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

    // Return color tag by class key
    function getTagColor(key) {
        let map = {
            "COMP 2080": "red",
            "COMP 4350": "blue",
            "COMP 4620": "green",
            "COMP 4380": "yellow",
        }
        let mapping = map[key];
        if(!mapping)
            return "grey";
        return mapping;
    }
    const reqs = ref([]);
    const chats = ref([]);

    let chatIndex = 0;
    const chat = ref(chats.value[0]);
    
    // Cycle through Buddy chat balloon conversations
    setInterval(()=>{
        chatIndex = (chatIndex + 1) % chats.value.length;
        chat.value = chats.value[chatIndex];
    },4000)

    onMounted(() => {
        setPageName("Dashboard");  
    })

    const classes = ref([]);
    const taskList = ref([]);
    const classTrigger = computed(() => {
        if(userId.value){
            const host = 'http://127.0.0.1:5000'; 
            let apiUrlClass = '/api/class';
            axios.get(host + apiUrlClass)
                .then(function (response) {
                    console.log(response);
                    let result = response.data.result;
                    classes.value = result;

                    // Get requirements from classes
                    let classList = result.map(c => c.class_Name);
                    for (let classKey of classList){
                        const apiUrlTask = `/api/class/${classKey}/task`;
                        axios.get(host + apiUrlTask)
                            .then(function (response) {
                                console.log(response);
                                // Handle null item defaults
                                let result = response.data.result;
                                for (let i=0; i<result.length; i++){
                                    if(!result[i].deadline)
                                        result[i].due = new Date(Date.now());
                                    else
                                        result[i].due = new Date(result[i].deadline);
                                    result[i].classKey = classKey;
                                    result[i].task_goal = "A";
                                    result[i].tagColor = getTagColor(classKey);
                                }
                                taskList.value = taskList.value.concat(result);
                            })
                            .catch(function (error) {
                                console.log(error.response);
                            })
                    }
                })
                .catch(function (error) {
                    console.log(error.response);
                    classes.value = [];
                })
        }
    })

    const taskTrigger = computed(() => {
        if(taskList.value.length > 0){
            reqs.value = filter.getReqs(taskList.value);
            chats.value = filter.getChats(taskList.value);
        }
    })
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
    <span>{{ classTrigger }}{{ taskTrigger }}</span>
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