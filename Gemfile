source "https://rubygems.org"

# To upgrade, run `bundle update github-pages`.
#gem "github-pages", group: :jekyll_plugins

# Required to include bibliography
#gem "jekyll-scholar", group: :jekyll_plugins

gem "minima", "~> 2.5"
# If you have any plugins, put them here!
group :jekyll_plugins do
    gem "jekyll", "~> 4.2.0"
    gem 'jekyll-archives'
    gem 'jekyll-scholar'
    gem 'jekyll-diagrams'
    gem 'jekyll-email-protect'
    gem 'jekyll-feed'
    gem 'jekyll-imagemagick'
    gem 'jekyll-minifier'
    gem 'jekyll-paginate-v2'
    gem 'jekyll-sitemap'
    gem 'jekyll-target-blank'
    gem 'jemoji'
    gem 'mini_racer'
    gem 'unicode_utils'
    gem 'webrick'
    gem "jekyll-katex"
end

group :other_plugins do
    gem 'httparty'
    gem 'feedjira'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]