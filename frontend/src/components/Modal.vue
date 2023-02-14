<script setup>
    import Happy from "/artifacts/happydog.svg";
    import Sad from "/artifacts/saddog.svg";
    import SuccessIcon from "/artifacts/success.svg";
    import FailureIcon from "/artifacts/error.svg";
    import { useStore } from "../stores";

    const store = useStore();
    const { toggleModal } = store;

    const props = defineProps({ 
        title: {type: String, required: false, default: "Modal Title"}
    })
</script>

<template>
    <div id="dog" :style="`background:url(${Happy});`" />
    <div id="modal">
        <div id="modal-title">
            <h1>{{ title }}</h1>
        </div>
        <span class="filler" />
        <span class="filler" />
        <span class="filler">
            <button class="close material-symbols-outlined" @click="toggleModal">
                close
            </button>
        </span>
        <div class="modal-content">
            <div id="modal-inner">
                <div id="modal-inner-content">
                    <slot />
                </div>
            </div>
        </div>
    </div>
    <div id="modal-overlay" @click="toggleModal"></div>
</template>

<style scoped>
    #modal-overlay{
        position: absolute;
        height: 100%;
        width: 100%;
        background: rgba(0,0,0,0.3);
        cursor: pointer;
    }

    #dog{
        position: absolute;
        z-index: 22;
        height: 5.5em;
        width: 5.5em;
        background-size: contain !important;
        background-repeat: no-repeat !important;
        left: 30%;
        top: 30%;
        transform: translate(-50%, -50%);
    }

    #modal{
        position: absolute;
        z-index: 21;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        height: max-content;
        width: 40vw;
        display: grid;
        justify-items: center;
        align-items: center;
        grid-template-columns: 15% 1fr 15%;
        grid-template-rows: auto 4vh auto;
        justify-items: center;
    }

    #modal-title{
        grid-column: 1/4;
        grid-row: 1/2;
        width: 70%;
        background: var(--box);
        text-align: center;
        border: 3px solid var(--border-gold);
        border-top-left-radius: 5em;
        border-top-right-radius: 5em;
        border-bottom-style: none;
        box-shadow: inset 0em 0.6em 0.5em rgba(0,0,0,0.4);
        line-height: 0.5;
    }

    .filler{
        height: 100%;
        width: 100%;
        grid-row: 2/3;
        background: var(--box);
        border: 3px solid var(--border-gold);
        border-bottom-style: none;
    }
    .filler:nth-child(2){
        border-top-left-radius: 2em;
    }
    .filler:nth-child(3){
        border-color: var(--box);
        border-right-style: none;
        z-index: 4;
    }
    .filler:nth-child(4){
        border-top-right-radius: 2em;
        background: var(--richgold);
        box-shadow: inset 0.2em -0.1em 0.8em rgba(0,0,0,0.4);
        font-size: 130%
    }


    .modal-content{
        grid-column: 1/4;
        grid-row: 3/4;
        width: 100%;
        background: var(--box);
        border: 3px solid var(--border-gold);
        border-bottom-left-radius: 2em;
        border-bottom-right-radius: 2em;
        border-top-style: none;
        display: grid;
        justify-items: center;
        align-items: center;
    }

    #modal-inner{
        width: 94%;
        margin: 1em;
        border: 1px solid var(--richgold);
        border-radius: 2em;
        background: var(--darkerteal);
        overflow-x: scroll;
    }

    #modal-inner-content{
        height: max-content;
        min-height: 50vh;
        max-height: 65vh;
        margin: 2vh 1vw 2vh 0;
        display: grid;
        justify-items: center;
        align-items: center;
        overflow-y: scroll;
    }

    .close{
        height: 100%;
        width: 100%;
        text-align: center;
        background: none;
        outline: none;
        border: none;
        color: var(--text);
    }

    @media screen and (max-width: 600px) {
        #modal{
            width: 90vw;
        }

        #dog{
            left: 10%;
            top: 30%;
        }
    }

</style>