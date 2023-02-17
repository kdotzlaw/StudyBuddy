/*
 * stores.js
 *    Pinia stores: Application-level state management.
 *    Used to store and export important refs and setter or getter functions that
 *    can be globally imported by any Vue component, module, or test suite.
 */

import { defineStore } from "pinia";
import { ref } from "vue";

export const useStore = defineStore('store', () => {

    /* sessionTimer
     *   Active session Timer class that stores user, class, and time elapsed
     *   setter @params - newTimer: Timer
     *=====================================*/
    const sessionTimer = ref(null);
    function setTimer(newTimer){
        sessionTimer.value = newTimer;
    }

    /* pageName
     *   Current page(route) name
     *   setter @params - newName: String 
     *=====================================*/
    const pageName = ref("Dashboard");
    function setPageName(newName){
        pageName.value = newName;
        return pageName.value
    }

    /* userId
     *   Authenticated user ID
     *   setter @params - newId: String
     *=====================================*/
    const userId = ref(null);
    function loginUser(newId){
        userId.value = newId;
    }
    function logoutUser(){  // unsetter
        userId.value = null;
        studyClass.value = null;
    }

    /* studyTime
     *   Time elapsed studying for session in seconds
     *   setter @params - time: Number
     *=====================================*/
    const studyTime = ref(0);
    function setStudyTime(time){
        if(time)
          studyTime.value = time;
    }

    /* studyClass
     *   Class being studied for in current Timer session
     *   setter @params - newClass: String
     *=====================================*/
    const studyClass = ref(null);
    function setStudyClass(newClass){
        studyClass.value = newClass;
    }

    /* isModalOpen
     *   Reflects if a modal is currently overlayed(toggled) on the app layout
     *   'Modified getter' toggleModal executes boolean negation and returns switched state
     *   getter @returns - Boolean
     *=====================================*/
    const isModalOpen = ref(false);
    function toggleModal(){
        isModalOpen.value = !isModalOpen.value;
        return isModalOpen.value;
    }

    /*   Manages modal display 
     *     modalTitle: Passed as a title prop to the Modal component
     *     modalContent: ID of the component or set of elements to display with ModalManager
     *     modalRender: HTML string to render inside the modal slot; Appears underneath modalContent
     *   setter @params - title: String, content: String, renderString: String
     *=====================================*/
    const modalTitle = ref("Modal Title");
    const modalContent = ref(null);
    const modalRender = ref("");
    function setModal(title="Modal Title", content=null, renderString=""){
        modalTitle.value = title;
        modalContent.value = content;
        modalRender.value = renderString;
        toggleModal();
    }

    /* uiSkin
     *   ID reference for custom background or component aesthetic styles
     *   setter @params - skin: String
     *=====================================*/
    const uiSkin = ref("skin-default");
    function updateSkin(skin="skin-default"){
        uiSkin.value = skin;
    }

    // Export refs and getter/setter functions
    return {
        sessionTimer, setTimer,
        pageName, setPageName,
        userId, loginUser, logoutUser,
        studyTime, studyClass, setStudyTime, setStudyClass,
        isModalOpen, toggleModal,
        modalTitle, modalContent, modalRender, setModal,
        uiSkin, updateSkin,
    }
})