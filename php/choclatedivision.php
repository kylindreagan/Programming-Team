<?php $replacedInput=str_replace(" ","*",fgets(STDIN));echo["Alf","Beata"][eval("return $replacedInput;")%2];?>
