const app = Vue.createApp({
    data() {
        return {
            cart: 0,
            product: 'Socks',
            selectedVariant: 0,
            description: 'A pair of warm, fuzzy socks',
            url: 'https:/github.com/macieljuniormax',
            inventory: 10,
            details: ['50% cotton', '30% wool', '20% polyester'],
            variants: [
                { id: 2234, color: 'green', image: './assets/images/socks_green.jpg', quantity: 0 },
                { id: 2235, color: 'blue', image: './assets/images/socks_blue.jpg', quantity: 10 }
            ],
            sizes: ['S', 'M', 'L', 'XL', 'XXL'],
            brand: 'Vue Mastery',
        }
    },

    methods: {
        addToCart() {
            this.cart += 1
        },
        updateVariant(index) {
            this.selectedVariant = index
        }
    },

    computed: {
        title() {
            return this.brand + ' ' + this.product
        },
        image() {
            return this.variants[this.selectedVariant].image
        },
        inStock() {
            return this.variants[this.selectedVariant].quantity
        }
    }
})
