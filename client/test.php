<?php
  session_start();
  $rtoken = $_COOKIE['cuicuiml_token'];
  $resultat = http_get("https://cui-cui.ml/api/get-results?code=" . $rtoken);
  var_dump($resultat);
  #var_dump($decoded_result);
  function console_log($output, $with_script_tags = true) {
      $js_code = 'console.log(' . json_encode($output, JSON_HEX_TAG) . 
  ');';
      if ($with_script_tags) {
          $js_code = '<script>' . $js_code . '</script>';
      }
      echo $js_code;
  }

  console_log($resultat)
?>