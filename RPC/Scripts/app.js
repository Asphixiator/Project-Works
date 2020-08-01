const game = ()=> {
    let p_score = 0;
    let c_score = 0;

    const startGame = ()=> {
        const startbtn = document.querySelector(".Intro button");
        const introscreen = document.querySelector(".Intro");
        const matchscreen = document.querySelector(".Match");
        const scorescreen = document.querySelector(".Score");

        startbtn.addEventListener("click", ()=> {
            introscreen.classList.add("FadeOut");
            scorescreen.classList.add("FadeIn");
            scorescreen.classList.remove("FadeOut");
            matchscreen.classList.add("FadeIn"); 
            matchscreen.classList.remove("FadeOut");
        });
    };

    const playMatch = ()=> {
        const playerchoice = document.querySelectorAll(".Choice button");
        const playerHand = document.querySelector(".PlayerHand");
        const computerHand = document.querySelector(".ComputerHand");
        const hands = document.querySelectorAll(".Hands img");

        hands.forEach((hand) => {
            hand.addEventListener("animationend", function() {
                this.style.animation = "";
            });
        });
        
        //get computer choice
        options = ["rock", "paper", "scissor"];

        playerchoice.forEach(function(option) {
            option.addEventListener("click", function() {
                console.log(this);
                const computer_number = Math.floor(Math.random() * 3);
                const computer_choice = options[computer_number];

                setTimeout(() => {
                    //Call compare function
                    compareHands(this.textContent, computer_choice);
                    //change the image of the hands
                    playerHand.src = `D:/HTML_Practice/RPC/Images/${this.textContent}.png`;
                    computerHand.src = `D:/HTML_Practice/RPC/Images/${computer_choice}.png`;
                }, 1000);

                //Animation
                playerHand.style.animation = "move-playerhand 1s ease";
                computerHand.style.animation = "move-computerhand 1s ease";
            });
        });

    }

    const updateScore = ()=> {
        const playerScore = document.querySelector(".PlayerScore p");
        const computerScore = document.querySelector(".ComputerScore p");
        playerScore.textContent = p_score;
        computerScore.textContent = c_score;
    }

    const compareHands = (player_choice, computer_choice)=> {
        const winner = document.querySelector(".Display");

        if (player_choice === computer_choice){
            winner.textContent = "Its a tie!";
            return;
        }
        else if (player_choice === "rock" && computer_choice === "paper") {
            winner.textContent = "Computer wins!";
            c_score++;
            updateScore();
            return;
        }
        else if (player_choice === "rock" && computer_choice === "scissor") {
            winner.textContent = "Player wins!";
            p_score++;
            updateScore();
            return;
        }
        else if (player_choice === "paper" && computer_choice === "rock") {
            winner.textContent = "Player wins!";
            p_score++;
            updateScore();
            return;
        }
        else if (player_choice === "paper" && computer_choice === "scissor") {
            winner.textContent = "Computer wins!";
            c_score++;
            updateScore();
            return;
        }
        else if (player_choice === "scissor" && computer_choice === "paper") {
            winner.textContent = "Player wins!";
            p_score++;
            updateScore();
            return;
        }
        else if (player_choice === "scissor" && computer_choice === "rock") {
            winner.textContent = "Computer wins!";
            c_score++;
            updateScore();
            return;
        }
    }

    startGame();
    playMatch();
};


game(); 

