+++
date = "2013-12-03T08:35:30+08:00"
draft = true
title = "snake game in ruby"

+++



<pre><code>
#!/usr/bin/env ruby

require "rubygame"
include Rubygame

def start_snake_game

  Rubygame.init

  screen = Screen.set_mode [400, 400]
  screen.title = "snack in ruby"
  screen.fill [0, 255, 0]
  screen.update
  unit = 20

  event_queue = EventQueue.new
  clock = Clock.new
  clock.target_framerate = 10

  snake = []
  3.times do |i|
    snake.insert(0,[i,0]) # the snake is (2,0) (1,0) (0,0)
  end
  food = [10,10] # the food is (10,10)
  move_up = false
  move_down = false
  move_left = false
  move_right = true
    
  game_over = false
  until game_over do
    event_queue.each do |event|
      case event
      when KeyDownEvent
        case event.key
        when K_ESCAPE # not K_ESC
          game_over = true
        when K_UP
          move_up = true
          move_down = false
          move_left = false
          move_right = false
        when K_DOWN
          move_up = false
          move_down = true
          move_left = false
          move_right = false
        when K_LEFT
          move_up = false
          move_down = false
          move_left = true
          move_right = false
        when K_RIGHT
          move_up = false
          move_down = false
          move_left = false
          move_right = true
        end
      when QuitEvent
        game_over = true
      end
    end
    puts snake
    (snake.length-1).times do |i| # most node move to it's the previous node's position
      index = snake.length - i - 1 # copy the snake from back to front
      snake[index][0] = snake[index-1][0]
      snake[index][1] = snake[index-1][1]
    end

    # move the head, 0 for x and 1 for y 
    if move_left == true
        snake[0][0] -=1
    end
    if move_right == true
        snake[0][0] += 1
    end
    if move_up == true
        snake[0][1] -= 1
    end
    if move_down == true
        snake[0][1] += 1
    end

    screen.fill [0, 255, 0]
    for node in snake # draw snake
      screen.draw_box_s([node[0]*unit, node[1]*unit], [(node[0]+1)*unit,(node[1]+1)*unit], [0, 0, 255])
    end

    screen.update
    clock.tick
   
  end

  Rubygame.quit
end

if __FILE__ == $0
  start_snake_game
end
</code></pre>