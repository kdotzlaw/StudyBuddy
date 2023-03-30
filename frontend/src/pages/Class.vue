<!-- 
  Class.vue
    route: /class
    Full-page class view to display meta class information, projected grade, and calendar requirements.
-->

<script setup>
    import { default as axios } from 'axios';
    import ArrowBack from "/artifacts/arrowback.svg";
    import Gear from "/artifacts/gear.svg";
    import Play from "/artifacts/play.svg";
    import Pause from "/artifacts/pausegold.svg";
    import RequirementCards from "../components/RequirementCards.vue";
    import Timer from "../logic/timer";
    import Mgmt from "../logic/managetimer";
    import { ref, computed, onMounted } from "vue";
    import { useRoute } from 'vue-router';
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { sessionTimer, userId, studyClass } = storeToRefs(store);
    const { updateSkin, setPageName, setStudyClass, setModal } = store;

    let classRoute = useRoute().params.slug;

    /*===========================
       MANAGE CLASS METADATA
     *===========================*/

    onMounted(() => {
        setPageName("Class View");

        // Get this class' metadata
        const host = 'http://127.0.0.1:5000'; 
        const apiUrlMeta = `/api/class/${classRoute}`;

        axios.get(host + apiUrlMeta)
            .then(function (response) {
                console.log(response);
                classInfo.value = response.data.result;
            })
            .catch(function (error) {
                console.log(error.response);
            })

        // Get this class' requirements
        const apiUrlReq = `/api/class/${classRoute}/task`;

        axios.get(host + apiUrlReq)
            .then(function (response) {
                console.log(response);
                reqs.value = response.data.result;
            })
            .catch(function (error) {
                console.log(error.response);
            })

        // Get this class' letter grade
        const apiUrlGrade = `/api/class/${classRoute}/grade`;

        axios.get(host + apiUrlGrade)
            .then(function (response) {
                console.log(response);
                let received = response.json();
                grade.value = received.data;
            })
            .catch(function (error) {
                console.log(error.response);
            })
    });

    const grade = ref("C+");
    const classInfo = ref({
        class_Name: "Loading...", // Class primary key
        studyTime: 0,
        classroom: null,
        prof_Name: null,
        prof_Email: null,
        prof_Phone: null,
        prof_Office: null,
        prof_Hours: null,
        section: null,
        timeslot: null
    });
    // Smart detect requirement type by checking keywords in title
    function getMatch(title){
        let matchList = [ 
            { 
                color: "green",
                matches: ["assignment", "homework", "hw"]
            },
            {
                color: "blue",
                matches: ["quiz", "assessment"]
            },
            {
                color: "red",
                matches: ["test", "exam", "midterm", "finals", "examination"]
            },
            {
                color: "yellow",
                matches: ["project", "report", "essay", "writeup", "presentation", "pitch"]
            }
        ]
        for(let list of matchList){
            for(let keyword of list.matches){
                if(title.includes(keyword))
                    return list.color
            }
        }
    }
    // Return color tag by req type
    function getTagColor(title) {
        let mapping = getMatch(title.toLowerCase());
        if(!mapping)
            return "grey";
        return mapping;
    }
    const reqs = ref([
        { name: "Quiz 5", tagColor: getTagColor("Quiz 5"), due: new Date("February 12, 2023"), goal: "C" },
        { name: "Homework 4", tagColor: getTagColor("Homework 4"), due: new Date("March 1, 2023"), goal: "C" },
        { name: "Quiz 6", tagColor: getTagColor("Quiz 6"), due: new Date("March 5, 2023"), goal: "B" },
        { name: "Assignment 5", tagColor: getTagColor("Assignment 5"), due: new Date("March 8, 2023"), goal: "C" },
        { name: "Midterm Exam", tagColor: getTagColor("Midterm Exam"), due: new Date("March 13, 2023"), goal: "B" },
        { name: "Final Project", tagColor: getTagColor("Final Project"), due: new Date("April 16, 2023"), goal: "C" },
        { name: "Final Exam", tagColor: getTagColor("Final Exam"), due: new Date("April 17, 2023"), goal: "C" },
        { name: "Become a Bee", tagColor: getTagColor("Become a Bee"), due: new Date("October 10, 2023"), goal: "" },
    ]);


    /*===========================
       STUDY SESSION PAUSE/PLAY
     *===========================*/

    // Start or pause study for this class
    function manageStudy(){
        setStudyClass(classRoute);
        Mgmt.manageTimer(userId.value,classRoute);
    }

    // Reflect study session's paused/running state with icons and notes
    const studyNote = computed(() => {
        if(studyClass.value == classRoute && !sessionTimer.value.isPaused())
            return "Pause session";
        return "Study now";
    });
    const studyIcon = computed(() => {
        if(studyClass.value == classRoute && !sessionTimer.value.isPaused())
            return Pause;
        return Play;
    });


    /*===========================
       FILTER REQUIREMENT CARDS
     *===========================*/

    // Present Date-time reference
    const current = ref(true);
    let today = Date.now();

    // Filter requirements by current(present-upcoming) or expired(past)
    const currentReqs = computed(() => {
        return reqs.value.filter(req => {
            let diffTime = req.due - today;
            let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            if(diffDays > -1)
                return req;
        })
    });
    const expiredReqs = computed(() => {
        return reqs.value.filter(req => {
            let diffTime = req.due - today;
            let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            if(diffDays < 0)
                return req;
        })
    });

    // Change displayed requirements based on active filter
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

    // Toggle between current/expired filter states
    function changeView(){
        current.value = !current.value;
    }

    function addRequirement(){
      setModal("Add Requirement", "addRequirement");
    }

</script>

<template>
    <div id="classpage">
        <section v-if="userId && reqs" id="hero">

            <!-- Back arrow to Dashboard -->
            <div id="back-items" v-motion-slide-right>
                <router-link to="/">
                    <button id="back">
                        <img :src="ArrowBack" alt="Go back to Dashboard" />
                        <span> Back </span>
                    </button>
                </router-link>

                <!-- Manage Class information -->
                <router-link :to="'/editClass/' + classRoute">
                    <img id="class-settings" :src="Gear" alt="Manage class information" />
                </router-link>

            </div>
            <div id="hero-items">
                <div>

                    <!-- Class name and time studied -->
                    <h1 v-motion-pop> {{ classRoute }} </h1>
                    <h2 v-motion-pop> Studied {{ classInfo.studyTime }} hours this week </h2>

                </div>
                <div v-motion-pop>

                    <!-- Study pause/play control -->
                    <button class="button round" @click="manageStudy">
                        <img id="study-ctrl" :src="studyIcon" :alt="studyNote" />
                    </button>
                    <span id="study-note"> {{ studyNote }} </span>

                </div>
            </div>
        </section>
        <section v-if="userId && reqs" id="class-items">

            <!-- Class requirements list -->
            <div id="req-ctr" v-motion-slide-left>
                <div id="req-head">
                    <button id="add-req" class="button bar" @click="addRequirement()">
                        Add Requirements
                    </button>
                    <button id="change-view" class="button bar" @click="changeView">
                        {{ viewNote }}
                    </button>
                </div>
                <RequirementCards :reqs="reqSet" />
            </div>

            <div>

                <!-- Class grade projection -->
                <div id="grade-ctr" v-motion-slide-right>
                    <h1 id="grade"> {{ grade }} </h1>
                    <div id="grade-note" class="delius">
                        Wow! <br/>
                        You are doing okay
                    </div>
                    <router-link :to="'/gradeCalculator/' + classRoute">
                      <button class="button bar">
                        Grade breakdown
                      </button>
                    </router-link>
                </div>

                <!-- Class meta details -->
                <div id="details-ctr" v-motion-slide-bottom>
                    <h3> Class Details </h3>
                    <table>
                        <tr>
                            <td> Name </td>
                            <td> {{ classInfo.class_Name }} </td>
                        </tr>
                        <tr>
                            <td> Timeslot </td>
                            <td> {{ classInfo.timeslot }} </td>
                        </tr>
                        <tr>
                            <td> Section </td>
                            <td> {{ classInfo.section }} </td>
                        </tr>
                        <tr>
                            <td> Room </td>
                            <td> {{ classInfo.classroom }} </td>
                        </tr>
                    </table>
                    
                    <h3> Professor Details </h3>
                    <table>
                        <tr>
                            <td> Name </td>
                            <td> {{ classInfo.prof_Name }} </td>
                        </tr>
                        <tr>
                            <td> Email </td>
                            <td> {{ classInfo.prof_Email }} </td>
                        </tr>
                        <tr>
                            <td> Phone </td>
                            <td> {{ classInfo.prof_Phone }} </td>
                        </tr>
                        <tr>
                            <td> Office Location </td>
                            <td> {{ classInfo.prof_Office }} </td>
                        </tr>
                        <tr>
                            <td> Office Hours </td>
                            <td> {{ classInfo.prof_Hours }} </td>
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

    td{
        margin: inherit;
        width: 100%;
        text-align: left;
    }

    @media screen and (max-width: 820px) {
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

        #class-items{
            display: flex;
            flex-direction: column;
            margin-left: 0;
            width: 90%;
        }
    }

</style>