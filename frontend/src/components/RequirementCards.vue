<!-- 
  RequirementCards.vue 
    Renders a set of cards from a user's requirements from classes. 
    Cards contain a req-specific color tag, due date, requirement name, grade goal, and Open Settings control.
-->

<script setup>
    import Gear from "/artifacts/gear.svg";
    import { computed } from "vue";
    import { useStore } from "../stores";
    
    const store = useStore();
    const {setModal, toggleModal} = store;

    const props = defineProps({ 
        reqs: {type: Array, required: false, default: []},
        borderless: {type: Boolean, required: false, default: false}
    })

    // Color tag and Month legend maps
    let today = Date.now();
    const monthNames = [
        "January", "February", "March", "April", 
        "May", "June", "July", "August", 
        "September", "October", "November", "December"
    ];

    /* getUrgent
     *   Adds an urgent note on cards with impending deadlines (0-3 days before due date) 
     *   @params - due: Date
     */
    function getUrgent(due){
        let diffTime = due - today;
        let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
        if (diffDays == 0)
            return "Due today";
        else if (diffDays == 1)
            return "Due tomorrow";
        else if (diffDays > 1 && diffDays < 4)
            return "Due in " + diffDays + " days";
        else
            return "";
    }

    // Borderless style
    let borderClass = computed(() => {
        if(props.borderless)
            return "borderless"
        return ""
    })
</script>

<template>
    <div id="reqCards" :class="borderClass">

        <!-- Requirement card set -->
        <div v-for="req in reqs" :class="`reqCard fullCard`">

            <!-- Color tag -->
            <div :class="`tag ${req.tagColor}`"></div>

            <!-- Due date -->
            <div class="dues">
                <h1 class="dueDate">
                    {{ req.due.getDate() }}
                </h1>
                <div class="dueMonth">
                    {{ monthNames[req.due.getMonth()] }}
                </div>
            </div>
            <div>

                <!-- Requirement name -->
                <h3> {{ req.name }} </h3>

                <p class="urgent"> {{ getUrgent(req.due) }} </p>
            </div>

            <!-- Grade goal -->
            <h2 class="goal"> {{ req.goal }} </h2>

            <!-- Open Settings control -->
            <img class="reqManage" :src="Gear" alt="Manage requirement" @click="setModal('Edit Requirement', 'editRequirement')" />

        </div>
    </div>
</template>

<style scoped>
    #reqCards{
        margin: 1em 0 2em 0;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;
    }

    .reqCard{
        height: 18vh;
        width: 100%;
        border-radius: 0.8em;
        margin: 0 0.5em 1em 0.5em;
        box-shadow: inset 0.1em 0.1em 0.3em rgba(0,0,0,0.4);
    }

    .addNew{
        border: 3px solid var(--border-disabled);
        color: var(--border-disabled);
        display: grid;
        justify-items: center;
        align-items: center;
        font-size: 30px;
        line-height: 30px;
        font-weight: 900;
    }

    .addNew:hover{
        transition: 0.5s ease-out;
        filter: brightness(120%);
    }

    .fullCard{
        border: 2px solid var(--gold);
        background: var(--box);
        display: grid;
        grid-template-columns: 2.5em 12% 1fr 4em 4em;
        grid-column-gap: 4%;
        overflow: hidden;
    }

    .fullCard .tag{
        height: 100%;
        width: 100%;
        box-shadow: inset -0.25em 0.2em 1.2em rgba(0,0,0,0.4);
    }

    .dues{
        display: flex;
        flex-direction: column;
        align-items: center;
        color: var(--gold);
        margin-bottom: 1em;
        align-self: center;
    }

    .dueDate{
        font-size: 48px;
        font-weight: 400;
        line-height: 0px;
    }

    .fullCard h3{
        color: var(--white);
        font-weight: 200;
        font-size: 30px;
        line-height: 1em;
        margin-top: 1.5em;
    }

    .urgent{
        color: var(--button-hover);
        line-height: 0px;
    }

    .goal, .reqManage{
        align-self: center;
    }

    .reqManage{
        height: 1.8em;
        width: 1.8em;
    }

    .reqManage:hover{
        transition: 0.3s;
        cursor: pointer;
        filter: brightness(120%);
        animation: spin 2s;
    }

    .borderless .fullCard{
        border: none;
        background: transparent;
        box-shadow: none;
        overflow: visible;
        margin-bottom: 2vh;
        transform: scale(0.9);
        font-size: 80%;
    }

    @media screen and (max-width: 820px) {
        #dashboard .fullCard{
            grid-template-columns: 2.5em 12% 1fr 3vw 3vw;
        }

        #dashboard .dueDate{
            font-size: 36px;
        }
        
        #dashboard .fullCard h3{
            font-size: 28px;
        }
    }

    @media screen and (max-width: 700px) {
        #classpage .fullCard{
            grid-template-columns: 2.5em 12% 1fr 3em 3em;
        }

        #classpage .dueDate{
            font-size: 36px;
        }

        #classpage .fullCard h3{
            font-size: 28px;
        }
    }
    
</style>