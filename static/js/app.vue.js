var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        band: {},
        albums: {},
        images: {},
        loadedImage: "static/img/placeholder.jpg",
        redStep: 0,
        greenStep: 0,
        blueStep: 0
    },
    methods: {
        fetchData: function() {
            this.$http.get('/testband').then(response => {
              this.band = response.body;
            }, response => {
                console.log("an error occurred");
            }).then(() => {
                this.$http.post('/testalbums', {params: {'band': this.band['title']}}).then(response => {
                  this.albums = response.body;
                }, response => {
                    console.log("an error occurred");
                });
              }
            )

            this.$http.get('/getInputImageFilenames').then(response => {
                this.images = response.body;
            })
        },
        loadImage: function(image) {
            this.$http.post('/loadImage', {params: {'image': image}}, {headers: {'Cache-Control': 'max-age=0, must-revalidate, no-store'}}).then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
            }, response => {
                console.log("an error occurred");
            });
        },
        addVLine: function() {
            this.$http.get('/addVLine').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        addHLine: function() {
            this.$http.get('/addHLine').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        shiftSubsetV: function() {
            this.$http.get('/shiftSubsetV').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        shiftSubsetH: function() {
            this.$http.get('/shiftSubsetH').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        fuzzify: function() {
            this.$http.get('/fuzzify').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        scanlineify: function() {
            this.$http.get('/scanlineify').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        bitify: function() {
            this.$http.get('/bitify').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        splitColors: function() {
            this.$http.get('/splitColors').then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
                console.log("successfully updated image")
            }, response => {
                console.log("an error occurred");
            })
        },
        shiftColor: function(color, direction, step) {
            this.$http.post('/shiftColor', {params: {'color': color, 'direction': direction, 'step': step}})
            .then(response => {
                let newImage = new Image();
                newImage.src = "static/img/out.jpg?" + new Date().getTime();
                this.loadedImage = newImage.src;
            }, response => {
                console.log("an error occurred");
            });
        }
    },
    mounted: function() {
        this.fetchData();
    }
})