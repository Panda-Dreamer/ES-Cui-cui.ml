<?php
    session_start();
    $id = $_GET['id'];
?>
<!DOCTYPE html>
<html> 
    <head>
        <meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Result - Cui-cui</title>
        <link rel="stylesheet" media="screen and (min-device-width: 11px)" href="styles/style_bird.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Noto+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Sen:wght@400;700;800&display=swap" rel="stylesheet">
        <script src= "handler2.js" defer="defer"></script>

	</head>
	<body>
		<nav>
            <div class="group_nav">
                <a href="/index.php"><img src="resources/nav_icon/home.svg" alt="home"></a>
                <a href"index.php"><div class="btn_micro">
                    <img src="resources/nav_icon/microphone.svg" alt="microphone">
                </div></a>
                <img src="resources/nav_icon/search.svg" alt="search">
            </div>
        </nav>
        <div class="up_bar_patch">
            <div class="up_bar">
                <a href="/result.php"><img src="resources/nav_icon/return.svg" alt="return"></a>
                <p class="title_page"><?=$_SESSION['decode_result']["name_" . $id]?></p>
                <img src="resources/nav_icon/nav_side.svg" alt="nav_side">
            </div>
        </div>
        <div class="block_command">
            <div class="group_command">
                <div class="btn_command">
                    <img src="resources/bird_page/play.svg" alt="play">
                </div>
                <a href="#overview">
                <div class="btn_command_2">
                    <img src="resources/bird_page/info.svg" alt="info">
                </div>
                </a>
                <a href="#title_images">
                <div class="btn_command">
                    <img src="resources/bird_page/images.svg" alt="images">
                </div>
                </a>
            </div>
            <img src="<?=$_SESSION['decode_result']["image_" . $id . "_1"]?>" alt="<?=$_SESSION['decode_result']["name_" . $id]?>" class="img_bird">
        </div>
        <div class="block_infos">
            <p class="name_bird"><?=$_SESSION['decode_result']["name_" . $id]?></p>
            <p id="overview">Aperçu</p>
            <p class="desc_bird"><?=$_SESSION['decode_result']["desc_" . $id]?></p>
            <p id="title_images">Images</p>
            <img src="<?=$_SESSION['decode_result']["image_" . $id . "_1"]?>" alt="<?=$_SESSION['decode_result']["name_" . $id]?>" class="images_bird">
            <img src="<?=$_SESSION['decode_result']["image_" . $id . "_2"]?>" alt="<?=$_SESSION['decode_result']["name_" . $id]?>" class="images_bird">
            <img src="<?=$_SESSION['decode_result']["image_" . $id . "_3"]?>" alt="<?=$_SESSION['decode_result']["name_" . $id]?>" class="images_bird">
            <p class="copyright">Toutes les images proviennent de : cornell.edu</p>
        </div>
        <div class="margin_nav_bar"></div>
    </body>
</html>
