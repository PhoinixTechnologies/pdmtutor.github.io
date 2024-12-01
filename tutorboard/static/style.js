    // Function to set progress on the circular indicator
    function setProgress(level) {
        const progressIndicator = document.querySelector('.progress-bar');

        //Calculating the offset for the given percentage
        const circleCircumference = 2 * Math.PI * 80;
        const offset = circleCircumference - (level / 100) * circleCircumference;

        // update circle
        progressIndicator.computedStyleMap.strokeDashoffset = offset;

        // function to fetch progress data from Node.js periodically
        async function fetchdata() {
            try{
                const response = await fetch('');
                const data = await response.json();
                setProgress(data.level)
            }
            catch (error) {
                console.error('Error fetching progress:', error);
            }
        }

        // Fetch the progress every 5 seconds which the params is in milliseconds hence the 5000;
        setInterval(fetchdata, 5000);

        // fetch on page load
        fetchdata();
    }
