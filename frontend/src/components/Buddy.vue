<!-- 
  Buddy.vue 
    Displays a choice of Buddy, and level card and conversations when enabled.
-->

<script setup>
    import TitleSq from "/artifacts/buddytemp.svg";
    import { storeToRefs } from "pinia";
    import { ref } from "vue";
    import { useMotion } from "@vueuse/motion";
    import { useStore } from "../stores";
    import Corgi from "./Corgi.vue";
    import Bunny from "./Bunny.vue";
    
    const store = useStore();
    const { buddyChoice } = storeToRefs(store);

    const props = defineProps({ 
        showLevel: {type: Boolean, required: false, default: false},
        chat: {type: String, required: false, default: null}
    })

    const buddy = ref(`<p>Buddy failed to load</p>`);
    const chatBalloon = ref();
    const chatBalloonCurve = ref();

    // Custom animation specs
    const chatAnimation = (initOpacity) => {
        return {
            initial: {
                x: -75,
                y: -15,
                rotate: -40,
                opacity: 0.5
            },
            enter: {
                x: 0,
                y: 0,
                rotate: 0,
                opacity: 1,
                transition:{
                    duration: 300,
                    ease: "easeIn"
                }
            }
        }
    }
    useMotion(chatBalloon, chatAnimation(0.5));
    useMotion(chatBalloonCurve, chatAnimation(0));
</script>

<template>

    <!-- Buddy container -->
    <div id="buddy">
        <div v-if="buddyChoice == 'Corgi'" >
            <Corgi />
        </div>
        <div v-else>
            <Bunny />
        </div>

        <!-- Chat balloon -->
        <div class="chat">
            <div v-if="props.chat" id="chat-balloon" class="delius" ref="chatBalloon">
                <p>{{ chat }}</p>
            </div>
            <div v-if="props.chat" id="chat-balloon-curve" ref="chatBalloonCurve"/>
        </div>
    </div>

    <!-- Level card -->
    <div v-if="showLevel" id="level-card" class="delius">
        Buddy the {{ buddyChoice }}
    </div>
    
</template>

<style scoped>
    #buddy{
        position: absolute;
        z-index: 2;
        top: 15%;
        width: 100%;
        display: grid;
        grid-template-columns: 50% 50%;
        margin-left: 35%;
    }

    #buddy svg{
        display: block;
        height: inherit;
        min-width: 14em;
        max-height: 17em;
        width: inherit;
    }

    .chat{
        height: 100%;
        width: 100%;
        transform: scale(0.9);
    }

    #chat-balloon{
        position: absolute;
        z-index: 5;
        top: -2em;
        min-height: 8em;
        height: max-content;
        width: 9em;
        background: var(--black);
        border-radius: 50%;
        padding: 0.5em 1.7em 0.5em 1.7em;
        display: grid;
        justify-items: center;
        align-items: center;
        text-align: center;
        overflow: hidden;
    }

    #chat-balloon-curve{
        position: absolute;
        z-index: 4;
        left: 0;
        top: 5em;
        height: 4em;
        width: 6em;
        background: radial-gradient(circle at top left, transparent 60%, var(--black) 61%);
        border-bottom-right-radius: 100%;
        transform: rotate(20deg);
    }

    #level-card{
        position: absolute;
        z-index: 2;
        bottom: 3.5em;
        background: var(--box);
        width: 50%;
        height: max-content;
        border-radius: 1em;
        padding: 2em;
        box-shadow: 0.4em 0.6em 1em rgba(0,0,0,0.4);
    }

    ellipse.shake{
        animation: shaking 8s ease-in-out infinite;
    }

    @keyframes shaking{
        0%,100%{
            transform: rotate(0deg);
        }
        50%{
            transform: rotate(4deg);
        }
    }
</style>