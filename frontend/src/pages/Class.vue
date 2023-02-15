<script setup>
    import ArrowBack from "/artifacts/arrowback.svg";
    import Gear from "/artifacts/gear.svg";
    import Pause from "/artifacts/pausegold.svg";
    import RequirementCards from "../components/RequirementCards.vue";
    import { onMounted } from "vue";
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { userId } = storeToRefs(store);
    const { updateSkin, setPageName } = store;

    onMounted(() => {
        setPageName("Class View");
    });

    // Stubbed requirements for now
    let reqs = [
        { name: "COMP2080", timeStudied: 2.5 },
        { name: "COMP4350", timeStudied: 6.2 },
        { name: "COMP4620", timeStudied: 0.0 },
        { name: "COMP4380", timeStudied: 10.0 },
    ]
</script>

<template>
    <div id="classpage">
        <section v-if="userId && reqs" id="hero">
            <div id="back-items">
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
                    <h1> COMP2080 </h1>
                    <h2> Studied 2 hours this week </h2>
                </div>
                <div>
                    <button class="button round">
                        <img id="study-ctrl" :src="Pause" alt="Pause study session" />
                    </button>
                    <span id="study-note"> Study now </span>
                </div>
            </div>
        </section>
        <section v-if="userId && reqs" id="class-items">
            <div id="req-ctr">
                <div id="req-head">
                    <button class="button bar">
                        Add Requirements
                    </button>
                    <button class="button bar">
                        View elapsed requirements
                    </button>
                </div>
                <RequirementCards />
            </div>
            <div>
                <div id="grade-ctr">
                    <h1 id="grade"> C+ </h1>
                    <div id="grade-note" class="delius">
                        Wow! <br/>
                        You are doing okay
                    </div>
                    <button class="button bar">
                        Grade breakdown
                    </button>
                </div>
                <div id="details-ctr">
                    <h3> Class Details </h3>
                    <table>
                        <tr>
                            <td> Name </td>
                            <td> Analysis of Algorithms </td>
                        </tr>
                        <tr>
                            <td> Section </td>
                            <td> A02 </td>
                        </tr>
                        <tr>
                            <td> Room </td>
                            <td> Armes 201 </td>
                        </tr>
                    </table>
                    
                    <h3> Professor Details </h3>
                    <table>
                        <tr>
                            <td> Name </td>
                            <td> Hello Surname </td>
                        </tr>
                        <tr>
                            <td> Email </td>
                            <td> hellosur@email.com </td>
                        </tr>
                        <tr>
                            <td> Phone </td>
                            <td> 204-505-6060 </td>
                        </tr>
                        <tr>
                            <td> Office Location </td>
                            <td> Machray 200 </td>
                        </tr>
                        <tr>
                            <td> Office Hours </td>
                            <td> 5:00-6:00 </td>
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

    #grade-ctr{
        width: 100%;
        background: var(--black);
        padding: 1.5em 0 1.5em 0;
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

    @keyframes spin{
        0%{
            transform: rotate(0deg);
        }
        100%{
            transform: rotate(360deg);
        }
    }

    @keyframes hop{
        0%,100%{
            transform: translateY(0px);
        }
        60%{
            transform: translateY(-15px);
        }
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