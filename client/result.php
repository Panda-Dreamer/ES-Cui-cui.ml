<?php
  session_start();

if($_SESSION['decode_result'] == ""){
$ch = curl_init();
$url = 'https://cui-cui.ml/api/get-results?code=' . $_COOKIE['cuicuiml_token'];
// Will return the response, if false it print the response
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// Set the url
curl_setopt($ch, CURLOPT_URL,$url);
// Execute
$result=curl_exec($ch);
// Closing
curl_close($ch);
// Will dump a beauty json :3
$_SESSION['decode_result'] = json_decode(html_entity_decode($result),true);
};


?>
<!DOCTYPE html>
<html> 
    <head>
        <meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Result - Cui-cui</title>
        <link rel="stylesheet" media="screen and (min-device-width: 11px)" href="styles/style_result.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <!--<script src= "js/script_anim.js" defer="defer"></script>-->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Noto+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Sen:wght@400;700;800&display=swap" rel="stylesheet">
	</head>
	<body>
		<nav>
            <div class="group_nav">
                <a href="/index.php"><img src="resources/nav_icon/home.svg" alt="home"></a>
                <div class="btn_micro">
                    <img src="resources/nav_icon/microphone.svg" alt="microphone">
                </div>
                <img src="resources/nav_icon/search.svg" alt="search">
            </div>
        </nav>
        <div class="up_bar_patch">
            <div class="up_bar">
                <a href="/index.php"><img src="resources/nav_icon/return.svg" alt="return"></a>
                <p class="title_page">Vos Résultats</p>
                <img src="resources/nav_icon/nav_side.svg" alt="nav_side">
            </div>
        </div>
        <div class="group_fonction">
            <?php 
                $count_tab = 1;
                while($count_tab <= $_SESSION['decode_result']['len']) {
                    $confiance = $_SESSION['decode_result']["conf_" . $count_tab];
                ?>
                    <a href="bird.php?id=<?= $count_tab ?>">
                        <div class="thumbnail">
                            <img src="<?= $_SESSION['decode_result']["image_" . $count_tab . "_1"] ?>" alt="<?= $_SESSION['decode_result']["name_" . $count_tab] ?>" class="img_thumbnail">
                            <p class="name_bird"><?= $_SESSION['decode_result']["name_" . $count_tab] ?></p>
                            <p class="probability"><?= intval($confiance) . "% de probabilité" ?></p>
                        </div>
                    </a>
                <?php
                    $count_tab += 1;
                }
            ?>
             
        </div>
        <div class="margin_nav_bar"></div>
    </body>
</html>
