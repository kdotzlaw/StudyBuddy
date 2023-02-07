import { defineStore } from "pinia";
import { ref } from "vue";

let stubContent = `
<p>Click anywhere outside modal to close</p>
<img src="/assets/title_sq.png" style="height:4em; width:4em;" alt="Study Buddy title" /> I am passed through a slot!
`;

export const useStore = defineStore('store', () => {
    // Toggle modal on and off
    const isModalOpen = ref(false);
    function toggleModal(){
        isModalOpen.value = !isModalOpen.value;
    }

    // Set modal contents
    const modalTitle = ref("Hey!");
    const modalContent = ref(stubContent);
    function setModal(title="Hey!", content=stubContent){
        modalTitle.value = title;
        modalContent.value = content;
        toggleModal();
    }

    // Change UI skin
    const uiSkin = ref("skin-default");
    function updateSkin(skin="skin-default"){
        uiSkin.value = skin;
    }

    return { 
        isModalOpen, toggleModal,
        modalTitle, modalContent, setModal,
        uiSkin, updateSkin,
    }
})