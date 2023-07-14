import minimax
import sys
import helper

# max_depth = int(sys.argv[1])
max_depth = 3
minimax.minimax(max_depth=max_depth,
                phase=2,
                static_estimate=helper.static_estimation_mid_improved,
                output_file_name="MiniMaxGameOutput.txt",
                player_color="White")
