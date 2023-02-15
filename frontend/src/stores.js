import { defineStore } from "pinia";
import { ref } from "vue";

let stubContent = `
<p>Click anywhere outside modal to close</p>
<img src="/assets/title_sq.png" style="height:4em; width:4em;" alt="Study Buddy title" /> I am passed through a slot!
`;

export const useStore = defineStore('store', () => {
    // Current page name
    const pageName = ref("Dashboard");
    function setPageName(newName){
        pageName.value = newName;
    }

    // User ID
    const userId = ref(null);
    function loginUser(newId){
        userId.value = newId;
    }
    function logoutUser(){
        userId.value = null;
        studyClass.value = null;
    }

    // Global timer state in seconds
    const studyTime = ref(0);
    function setStudyTime(time){
        if(time)
            studyTime.value = time;
    }

    // Class being studied
    const studyClass = ref(null);
    function setStudyClass(newClass){
        studyClass.value = newClass;
    }

    // Toggle modal on and off
    const isModalOpen = ref(false);
    function toggleModal(){
        isModalOpen.value = !isModalOpen.value;
    }

    // Set modal contents
    const modalTitle = ref("Modal Title");
    const modalContent = ref(null);
    const modalRender = ref("");
    function setModal(title="Modal Title", content=null, renderString=""){
        modalTitle.value = title;
        modalContent.value = content;
        modalRender.value = renderString;
        toggleModal();
    }

    // Change UI skin
    const uiSkin = ref("skin-default");
    function updateSkin(skin="skin-default"){
        uiSkin.value = skin;
    }

    return { 
        pageName, setPageName,
        userId, loginUser, logoutUser,
        studyTime, studyClass, setStudyTime, setStudyClass,
        isModalOpen, toggleModal,
        modalTitle, modalContent, modalRender, setModal,
        uiSkin, updateSkin,
    }
})