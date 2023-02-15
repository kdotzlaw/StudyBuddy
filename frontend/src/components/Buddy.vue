<script setup>
    import TitleSq from "/artifacts/buddytemp.svg"
    import { ref } from "vue";

    const props = defineProps({ 
        showLevel: {type: Boolean, required: false, default: false},
        chat: {type: String, required: false, default: null}
    })

    const buddy = ref(`<p>Buddy failed to load</p>`);

    // Fetch your animated SVG buddy!
    ;(async ()=>{
        const res = await fetch(TitleSq);
        const src = await res.text();
        buddy.value = src;
    })()
</script>

<template>
    <div id="buddy" v-html="buddy" />
    <div v-if="props.chat" id="chat-balloon" class="delius">
        <p>{{ chat }}</p>
    </div>
    <div id="chat-balloon-curve" />
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
        right: 22%;
        top: 20%;
        height: 4em;
        width: 6em;
        background: radial-gradient(circle at top left, transparent 60%, var(--black) 61%);
        border-bottom-right-radius: 100%;
        transform: rotate(20deg);
    }

    #level-card{
        position: absolute;
        z-index: 2;
        top: 50%;
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