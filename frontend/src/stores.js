import { defineStore } from "pinia";
import { ref } from "vue";

export const useStore = defineStore('store', () => {
    // Toggle modal on and off
    const isModalOpen = ref(false);
    function toggleModal(){
        isModalOpen.value = !isModalOpen.value;
    }

    return { 
        isModalOpen, toggleModal
    }
})