
export default {
    template: `
        <button 
            :class="{
                'px-4 py-2 border rounded': true,
                'bg-blue-600 hover:bg-blue-700': type === 'primary',
                'bg-gray-200 hover:bg-gray-400': type === 'secondary',
                'bg-purple-200 hover:bg-purple-400': type === 'muted',
                'is-loading': processing,
            }" 
            v-model:disabled="processing">
            <slot/> </button>
    `,

    props:{
        type:{
            type: String,
            default: 'primary',
        },

        processing:{
            type: Boolean,
            default: false,
        }
    },

}