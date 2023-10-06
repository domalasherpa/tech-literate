
export default {
    template: `
        <button class="bg-gray-200 hover:bg-gray-400 px-4 py-2 border rounded" v-model:disabled="processing">
            <slot/> </button>
    `,

    props:{
        type:{
            type: String,
            default: 'primary',
        }
    },

    data(){
        return{
            'processing': false,
        };
    }
    
}