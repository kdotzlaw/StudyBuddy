<script setup>
    import ArrowBack from "/artifacts/arrowback.svg";
    import Gear from "/artifacts/gear.svg";
    import Play from "/artifacts/play.svg";
    import Pause from "/artifacts/pausegold.svg";
    import RequirementCards from "../components/RequirementCards.vue";
    import Timer from "../logic/timer";
    import Mgmt from "../logic/managetimer";
    import { ref, computed, onMounted } from "vue";
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { sessionTimer, userId, studyClass } = storeToRefs(store);
    const { updateSkin, setPageName, setStudyClass } = store;

    onMounted(() => {
        setPageName("Class View");
    });

    // Stubbed requirements for now
    let reqs = [
        { name: "Quiz 5", type: "quiz", due: new Date("February 12, 2023"), goal: "C" },
        { name: "Catch up", type: "haha", due: new Date("February 17, 2023"), goal: "C" },
        { name: "Assignment 4", type: "assignment", due: new Date("March 1, 2023"), goal: "C" },
        { name: "Quiz 6", type: "quiz", due: new Date("March 5, 2023"), goal: "B" },
        { name: "Assignment 5", type: "assignment", due: new Date("March 8, 2023"), goal: "C" },
        { name: "Midterm Exam", type: "test", due: new Date("March 9, 2023"), goal: "B" },
        { name: "Become a Bee", type: "dne", due: new Date("October 10, 2023"), goal: "" },
    ]

    let classInfo = {
        name: "COMP2080", // primary key
        timeStudied: 2.3,
        grade: "C+",
        details: {
            name: "Analysis of Algorithms",
            section: "A02",
            room: "Armes 201"
        },
        professor: {
            name: "Hello surname",
            email: "hellosur@email.com",
            phone: "204-505-6060",
            officeLocation: "Machray 200",
            officeHours: "5:00-6:00"
        }
    }

    // Reflect study state
    const studyNote = computed(() => {
        if(studyClass.value == classInfo.name && !sessionTimer.value.isPaused())
            return "Pause session";
        return "Study now";
    });
    const studyIcon = computed(() => {
        if(studyClass.value == classInfo.name && !sessionTimer.value.isPaused())
            return Pause;
        return Play;
    });

    // Filter requirements by current or expired
    const current = ref(true);
    let today = Date.now();

    const currentReqs = computed(() => {
        return reqs.filter(req => {
            let diffTime = req.due - today;
            let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            if(diffDays > -1)
                return req;
        })
    });

    const expiredReqs = computed(() => {
        return reqs.filter(req => {
            let diffTime = req.due - today;
            let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            if(diffDays < 0)
                return req;
        })
    });

    function changeView(){
        current.value = !current.value;
    }

    // Filter by current or expired requirements
    const reqSet = computed(() => {
        if(current.value)
            return currentReqs.value;
        return expiredReqs.value;
    });

    const viewNote = computed(() => {
        if(current.value)
            return "View expired requirements";
        return "View current requirements";
    });

    // Start or pause study for this class
    function manageStudy(){
        setStudyClass(classInfo.name);
        Mgmt.manageTimer(userId.value,classInfo.name);
    }
</script>

<template>
    <div id="classpage">
        <section v-if="userId && reqs" id="hero">
            <div id="back-items" v-motion-slide-right>
                <router-link to="/">
                    <button id="back">
                        <img :src="ArrowBack" alt="Go back to Dashboard" />
                        <span> Back </span>
                    </button>
                </router-link>
                <img id="class-settings" :src="Gear" alt="Manage class information" />
            </div>
            <div id="hero-items">
                <div>
                    <h1 v-motion-pop> {{ classInfo.name }} </h1>
                    <h2 v-motion-pop> Studied {{ classInfo.timeStudied }} hours this week </h2>
                </div>
                <div v-motion-pop>
                    <button class="button round" @click="manageStudy">
                        <img id="study-ctrl" :src="studyIcon" :alt="studyNote" />
                    </button>
                    <span id="study-note"> {{ studyNote }} </span>
                </div>
            </div>
        </section>
        <section v-if="userId && reqs" id="class-items">
            <div id="req-ctr" v-motion-slide-left>
                <div id="req-head">
                    <button id="add-req" class="button bar">
                        Add Requirements
                    </button>
                    <button id="change-view" class="button bar" @click="changeView">
                        {{ viewNote }}
                    </button>
                </div>
                <RequirementCards :reqs="reqSet" />
            </div>
            <div>
                <div id="grade-ctr" v-motion-slide-right>
                    <h1 id="grade"> {{ classInfo.grade }} </h1>
                    <div id="grade-note" class="delius">
                        Wow! <br/>
                        You are doing okay
                    </div>
                    <button class="button bar">
                        Grade breakdown
                    </button>
                </div>
                <div id="details-ctr" v-motion-slide-bottom>
                    <h3> Class Details </h3>
                    <table>
                        <tr>
                            <td> Name </td>
                            <td> {{ classInfo.details.name }} </td>
                        </tr>
                        <tr>
                            <td> Section </td>
                            <td> {{ classInfo.details.section }} </td>
                        </tr>
                        <tr>
                            <td> Room </td>
                            <td> {{ classInfo.details.room }} </td>
                        </tr>
                    </table>
                    
                    <h3> Professor Details </h3>
                    <table>
                        <tr>
                            <td> Name </td>
                            <td> {{ classInfo.professor.name }} </td>
                        </tr>
                        <tr>
                            <td> Email </td>
                            <td> {{ classInfo.professor.email }} </td>
                        </tr>
                        <tr>
                            <td> Phone </td>
                            <td> {{ classInfo.professor.phone }} </td>
                        </tr>
                        <tr>
                            <td> Office Location </td>
                            <td> {{ classInfo.professor.officeLocation }} </td>
                        </tr>
                        <tr>
                            <td> Office Hours </td>
                            <td> {{ classInfo.professor.officeHours }} </td>
                        </tr>
                    </table>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
    #class{
        width: 95%;
        display: flex;
        justify-content: space-between;
        margin: 5vh 0 10vh 0;
    }

    #hero{
        position: relative;
        margin-top: 2vh;
        height: 35vh;
        width: 100%;
    }

    #back-items{
        position: absolute;
        z-index: 4;
        display: flex;
        align-items: center;
    }

    #back{
        display: flex;
        align-items: center;
        background: none;
        outline: none;
    }

    #back img, #study-ctrl{
        height: 40%;
        width: 40%;
    }

    #back span{
        font-weight: 800;
        font-size: 20px;
        color: var(--gold);
        margin-left: 5%;
    }

    #class-settings{
        height: 1.3em;
        width: 1.3em;
    }

    #class-settings:hover{
        transition: 0.3s;
        cursor: pointer;
        filter: brightness(120%);
        animation: spin 2s;
    }

    #back:active, #class-settings:active{
        animation: hop 0.5s ease-in-out;
    }

    #hero-items{
        position: absolute;
        z-index: 3;
        left: 55%;
        top: 40%;
        transform: translate(-50%,-50%);
        width: max-content;
        display: grid;
        justify-items: center;
        grid-template-columns: max-content 1fr;
    }

    #hero-items div{
        display: flex;
        align-items: center;
    }
    #hero-items div:nth-child(1){
        flex-direction: column;
        transform: translateY(1em);
    }

    #hero-items h1, #hero-items h2{
        font-weight: 400;
        line-height: 40px;
    }

    #hero-items h1, #grade{
        font-size: 72px;
        letter-spacing: 5px;
        margin: 0;
    }

    #hero-items div:nth-child(2){
        width: 15em;
        margin-left: 3em;
    }

    .button{
        background: var(--button);
        border: 3px solid var(--gold);
        box-shadow: inset 0.2em 0.2em 0.6em rgba(0,0,0,0.4);
        display: grid;
        justify-items: center;
        align-items: center;
        color: var(--gold);
        border-radius: 1em;
        font-family: 'Croissant One', cursive;
    }

    .button:hover{
        transition: 0.3s;
        background: var(--button-shade);
    }

    .round{
        height: 7em;
        width: 7em;
        border-radius: 50%;
    }

    .bar{
        padding: 0.7em 2.3em 0.7em 2.3em;
    }

    #study-note{
        color: var(--gold);
        margin-left: 4%;
    }

    #class-items{
        display: grid;
        grid-template-columns: 55% 25%;
        grid-column-gap: 8%;
        margin-left: 8%;
    }

    #req-head{
        width: 90%;
        margin-left: 5%;
        display: flex;
        justify-content: space-between;
    }

    #change-view{
        background: var(--lightteal);
        border: 1px solid var(--black);
        border-radius: 0;
        box-shadow: none;
        color: var(--text-disabled);
    }

    #change-view:hover{
        transition: 0.3s;
        background: var(--teal);
    }

    #grade-ctr{
        width: 100%;
        background: var(--black);
        padding: 1.5em 0 2.5em 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 2em;
    }

    #grade-note{
        text-align: center;
        line-height: 32px;
        margin: 6vh 0 4vh 0;
    }

    #details-ctr{
        background: var(--box);
        border: 2px solid var(--black);
        padding: 0 0.6em 1em 1em;
        margin: 3vh 0 5vh 0;
    }

    #details-ctr table{
        width: 100%;
    }

    @media screen and (max-width: 800px) {
        #hero{
            height: 80vh;
        }

        #hero-items{
            display: flex;
            top: 50%;
            left: 45%;
            flex-direction: column;
            justify-items: center;
            align-items: center;
        }

        #hero-items div:nth-child(2){
            margin: 2em 0 0 3em;
        }
    }

</style>