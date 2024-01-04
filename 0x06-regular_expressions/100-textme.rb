#!/usr/bin/env ruby
sender = ARGV[0].scan(/(?<=from:)(\W?\w+)/).join
receiver = ARGV[0].scan(/(?<=to:)\W?\w+/).join
flags = ARGV[0].scan(/(?<=flags:)(.?\d..?\d..?\d..?\d..?\d)/).join
puts("#{sender},#{receiver},#{flags}")
