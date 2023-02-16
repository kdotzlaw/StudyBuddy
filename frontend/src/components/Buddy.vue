<script setup>
    import TitleSq from "/artifacts/buddytemp.svg";
    import Corgi from "./Corgi.vue";
    import { ref } from "vue";
    import { useMotion } from "@vueuse/motion";

    const props = defineProps({ 
        showLevel: {type: Boolean, required: false, default: false},
        chat: {type: String, required: false, default: null}
    })

    const buddy = ref(`<p>Buddy failed to load</p>`);
    const chatBalloon = ref();
    const chatBalloonCurve = ref();

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
    <div id="buddy">
        <Corgi />
    </div>
    <div v-if="props.chat" id="chat-balloon" class="delius" ref="chatBalloon">
        <p>{{ chat }}</p>
    </div>
    <div v-if="props.chat" id="chat-balloon-curve" ref="chatBalloonCurve"/>
    <div v-if="showLevel" id="level-card" class="delius">
        Level 0
    </div>
</template>

<style scoped>
    #buddy{
        position: absolute;
        z-index: 2;
        top: 10%;
        transform: translateX(-15%);
    }

    #buddy svg{
        display: block;
        height: inherit;
        width: inherit;
    }

    #chat-balloon{
        position: absolute;
        z-index: 4;
        right: 0;
        height: 8em;
        width: 9em;
        background: var(--black);
        border-radius: 50%;
        padding: 0 1.5em 0 1.5em;
        display: grid;
        justify-items: center;
        align-items: center;
        text-align: center;
        overflow: hidden;
    }

    #chat-balloon-curve{
        position: absolute;
        z-index: 4;
        right: 7em;
        top: 6em;
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