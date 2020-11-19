# AdminBot
A Moderation and General Discord Bot for Server Management and Fun!

***

You'll want to replace the values with your own.  The `prefix` key can be omitted, and the bot will fallback on its default `$` prefix.

***

# Command List

A list of cogs, commands, and descriptions:

[Actions](#actions), [Admin](#admin), [Ascii](#ascii), [Bot](#bot), [BotAdmin](#botadmin), [CAH](#cah), [Calc](#calc), [Channel](#channel), [ChatterBot](#chatterbot), [Claptrap](#claptrap), [Clippy](#clippy), [CogManager](#cogmanager), [Comic](#comic), [DJRoles](#djroles), [Debugging](#debugging), [DisableCommand](#disablecommand), [DrBeer](#drbeer), [EightBall](#eightball), [Emoji](#emoji), [Encode](#encode), [Example](#example), [Face](#face), [Feed](#feed), [Fliptime](#fliptime), [GameLookup](#gamelookup), [Giphy](#giphy), [Groot](#groot), [Help](#help), [Humor](#humor), [Hw](#hw), [IntelArk](#intelark), [Invite](#invite), [Jpeg](#jpeg), [LangFilter](#langfilter), [Lists](#lists), [MadLibs](#madlibs), [Morse](#morse), [Music](#music), [OfflineUser](#offlineuser), [PciUsb](#pciusb), [Plist](#plist), [Printer](#printer), [Profile](#profile), [Promote](#promote), [Quote](#quote), [RateLimit](#ratelimit), [Reddit](#reddit), [Remind](#remind), [Search](#search), [SecretSanta](#secretsanta), [Server](#server), [ServerStats](#serverstats), [Settings](#settings), [Setup](#setup), [Spooktober](#spooktober), [Stream](#stream), [Strike](#strike), [Tags](#tags), [Telephone](#telephone), [TempRole](#temprole), [Time](#time), [Translate](#translate), [Turret](#turret), [Uptime](#uptime), [UrbanDict](#urbandict), [UserRole](#userrole), [VoteKick](#votekick), [Weather](#weather), [Welcome](#welcome), [Wiki](#wiki), [Xp](#xp), [XpBlock](#xpblock), [XpStack](#xpstack)

## Actions
####	Actions Cog (6 commands) - Actions.py Extension:
	  $boop [member]
	   └─ Boop da snoot.
	  $drink [member]
	   └─ Drink like a boss.
	  $eat [member]
	   └─ Eat like a boss.
	  $highfive [member]
	   └─ High five like a boss.
	  $pet [member]
	   └─ pet kitties.
	  $spook [member]
	   └─ sp00ktober by camiel.

## Admin
####	Admin Cog (26 commands) - Admin.py Extension:
	  $addadmin [role]
	   └─ Adds a new role to the admin list (admin only).
	  $addxprole [role] [xp]
	   └─ Adds a new role to the xp promotion/demotion system (admin only).
	  $broadcast [message]
	   └─ Broadcasts a message to all connected servers.  Can only be done by the owner.
	  $defaultchannel 
	   └─ Lists the server's default channel, whether custom or not.
	  $lock 
	   └─ Toggles whether the bot only responds to admins (admin only).
	  $onexprole [yes_no]
	   └─ Gets and sets whether or not to remove all but the current xp role a user has...
	  $prunexproles 
	   └─ Removes any roles from the xp promotion/demotion system that are no longer on...
	  $rawrules 
	   └─ Display the markdown for the server's rules (bot-admin only).
	  $removeadmin [role]
	   └─ Removes a role from the admin list (admin only).
	  $removemotd [chan]
	   └─ Removes the message of the day from the selected channel.
	  $removexprole [role]
	   └─ Removes a role from the xp promotion/demotion system (admin only).
	  $setdefaultchannel [channel]
	   └─ Sets a replacement default channel for bot messages (admin only).
	  $setdefaultrole [role]
	   └─ Sets the default role or position for auto-role assignment.
	  $sethackrole [role]
	   └─ Sets the required role ID to add/remove hacks (admin only).
	  $setlinkrole [role]
	   └─ Sets the required role ID to add/remove links (admin only).
	  $setmadlibschannel [channel]
	   └─ Sets the channel for MadLibs (admin only).
	  $setmotd [message] [chan]
	   └─ Adds a message of the day to the selected channel.
	  $setrules [rules]
	   └─ Set the server's rules (bot-admin only).
	  $setstoprole [role]
	   └─ Sets the required role ID to stop the music player (admin only).
	  $setxp [member] [xpAmount]
	   └─ Sets an absolute value for the member's xp (admin only).
	  $setxpreserve [member] [xpAmount]
	   └─ Set's an absolute value for the member's xp reserve (admin only).
	  $setxprole [role]
	   └─ Sets the required role ID to give xp, gamble, or feed the bot (admin only).
	  $stoprole 
	   └─ Lists the required role to stop the bot from playing music.
	  $xplimit [limit]
	   └─ Gets and sets a limit to the maximum xp a member can get.  Pass a negative va...
	  $xpreservelimit [limit]
	   └─ Gets and sets a limit to the maximum xp reserve a member can get.  Pass a neg...
	  $xprole 
	   └─ Lists the required role to give xp, gamble, or feed the bot.

## Ascii
####	Ascii Cog (1 command) - Ascii.py Extension:
	  $ascii [text]
	   └─ Beautify some text (font list at http://artii.herokuapp.com/fonts_list).

## Bot
####	Bot Cog (23 commands) - Bot.py Extension:
	  $adminunlim [yes_no]
	   └─ Sets whether or not to allow unlimited xp to admins (owner only).
	  $avatar [filename]
	   └─ Sets the bot's avatar (owner only).
	  $basadmin [yes_no]
	   └─ Sets whether or not to treat bot-admins as admins with regards to xp (admin o...
	  $botinfo 
	   └─ Lists some general stats about the bot.
	  $cloc 
	   └─ Outputs the total count of lines of code in the currently installed repo.
	  $embed [embed_type=field] <embed>
	   └─ Builds an embed using json formatting.
	  $getimage <image>
	   └─ Tests downloading - owner only
	  $hostinfo 
	   └─ List info about the bot's host environment.
	  $joinpm [yes_no]
	   └─ Sets whether or not to pm the rules to new users when they join (bot-admin on...
	  $listengame [game]
	   └─ Sets the listening status of the bot (owner-only).
	  $nickname [name]
	   └─ Set the bot's nickname (admin-only).
	  $ping 
	   └─ Feeling lonely?
	  $playgame [game]
	   └─ Sets the playing status of the bot (owner-only).
	  $pres [playing_type=0] [status_type=online] [game] [url]
	   └─ Changes the bot's presence (owner-only).
	  $reboot [force]
	   └─ Reboots the bot (owner only).
	  $servers 
	   └─ Lists the number of servers I'm connected to!
	  $setbotparts [parts]
	   └─ Set the bot's parts - can be a url, formatted text, or nothing to clear.
	  $shutdown [force]
	   └─ Shuts down the bot (owner only).
	  $source 
	   └─ Link the github source.
	  $speedtest 
	   └─ Run a network speed test (owner only).
	  $status [status]
	   └─ Gets or sets the bot's online status (owner-only).
	  $streamgame [url] [game]
	   └─ Sets the streaming status of the bot, requires the url and the game (owner-on...
	  $watchgame [game]
	   └─ Sets the watching status of the bot (owner-only).

## BotAdmin
####	BotAdmin Cog (8 commands) - BotAdmin.py Extension:
	  $ban [member]
	   └─ Bans the selected member (bot-admin only).
	  $ignore [member]
	   └─ Adds a member to the bot's "ignore" list (bot-admin only).
	  $ignored 
	   └─ Lists the users currently being ignored.
	  $kick [member]
	   └─ Kicks the selected member (bot-admin only).
	  $listen [member]
	   └─ Removes a member from the bot's "ignore" list (bot-admin only).
	  $mute [member] [cooldown]
	   └─ Prevents a member from sending messages in chat (bot-admin only).
	  $setuserparts [member] [parts]
	   └─ Set another user's parts list (owner only).
	  $unmute [member]
	   └─ Allows a muted member to send messages in chat (bot-admin only).

## CAH
####	CAH Cog (17 commands) - CAH.py Extension:
	  $addbot 
	   └─ Adds a bot to the game.  Can only be done by the player who created the game.
	  $addbots [number]
	   └─ Adds bots to the game.  Can only be done by the player who created the game.
	  $cahgames 
	   └─ Displays up to 10 CAH games in progress.
	  $flushhand 
	   └─ Flushes the cards in your hand - can only be done once per game.
	  $game [message]
	   └─ Displays the game's current status.
	  $hand 
	   └─ Shows your hand.
	  $idlekick [setting]
	   └─ Sets whether or not to kick members if idle for 5 minutes or more.  Can only ...
	  $joincah [id]
	   └─ Join a Cards Against Humanity game.  If no id or user is passed, joins a rand...
	  $laid 
	   └─ Shows who laid their cards and who hasn't.
	  $lay [card]
	   └─ Lays a card or cards from your hand.  If multiple cards are needed, separate ...
	  $leavecah 
	   └─ Leaves the current game you're in.
	  $newcah 
	   └─ Starts a new Cards Against Humanity game.
	  $pick [card]
	   └─ As the judge - pick the winning card(s).
	  $removebot [id]
	   └─ Removes a bot from the game.  Can only be done by the player who created the ...
	  $removeplayer [name]
	   └─ Removes a player from the game.  Can only be done by the player who created t...
	  $say [message]
	   └─ Broadcasts a message to the other players in your game.
	  $score 
	   └─ Display the score of the current game.

## Calc
####	Calc Cog (1 command) - Calc.py Extension:
	  $calc [formula]
	   └─ Do some math.

## Channel
####	Channel Cog (7 commands) - Channel.py Extension:
	  $islocked 
	   └─ Says whether the bot only responds to admins.
	  $ismuted [member]
	   └─ Says whether a member is muted in chat.
	  $listadmin 
	   └─ Lists admin roles and id's.
	  $listmuted 
	   └─ Lists the names of those that are muted.
	  $log [messages=25] [chan]
	   └─ Logs the passed number of messages from the given channel - 25 by default (ad...
	  $rolecall [role]
	   └─ Lists the number of users in a current role.
	  $rules 
	   └─ Display the server's rules.

## ChatterBot
####	ChatterBot Cog (2 commands) - ChatterBot.py Extension:
	  $chat [message]
	   └─ Chats with the bot.
	  $setchatchannel [channel]
	   └─ Sets the channel for bot chatter.

## Claptrap
####	Claptrap Cog (1 command) - Claptrap.py Extension:
	  $claptrap 
	   └─ Can I shoot something now? Or climb some stairs? SOMETHING exciting?

## Clippy
####	Clippy Cog (1 command) - Clippy.py Extension:
	  $clippy [text]
	   └─ I *know* you wanted some help with something - what was it?

## CogManager
####	CogManager Cog (5 commands) - CogManager.py Extension:
	  $extension [extension]
	   └─ Outputs the cogs attatched to the passed extension.
	  $extensions 
	   └─ Lists all extensions and their corresponding cogs.
	  $imports [extension]
	   └─ Outputs the extensions imported by the passed extension.
	  $reload [extension]
	   └─ Reloads the passed extension - or all if none passed.
	  $update 
	   └─ Updates from git.

## Comic
####	Comic Cog (14 commands) - Comic.py Extension:
	  $calvin [date]
	   └─ Displays the Calvin & Hobbes comic for the passed date (MM-DD-YYYY) if found.
	  $cyanide [date]
	   └─ Displays the Cyanide & Happiness comic for the passed date (MM-DD-YYYY) if fo...
	  $dilbert [date]
	   └─ Displays the Dilbert comic for the passed date (MM-DD-YYYY).
	  $garfield [date]
	   └─ Displays the Garfield comic for the passed date (MM-DD-YYYY) if found.
	  $gmg [date]
	   └─ Displays the Garfield Minus Garfield comic for the passed date (MM-DD-YYYY) i...
	  $peanuts [date]
	   └─ Displays the Peanuts comic for the passed date (MM-DD-YYYY) if found.
	  $randcalvin 
	   └─ Randomly picks and displays a Calvin & Hobbes comic.
	  $randcyanide 
	   └─ Randomly picks and displays a Cyanide & Happiness comic.
	  $randgarfield 
	   └─ Randomly picks and displays a Garfield comic.
	  $randgmg 
	   └─ Randomly picks and displays a Garfield Minus Garfield comic.
	  $randilbert 
	   └─ Randomly picks and displays a Dilbert comic.
	  $randpeanuts 
	   └─ Randomly picks and displays a Peanuts comic.
	  $randxkcd 
	   └─ Displays a random XKCD comic.
	  $xkcd [date]
	   └─ Displays the XKCD comic for the passed date (MM-DD-YYYY) or comic number if f...

## DJRoles
####	DJRoles Cog (4 commands) - DJRoles.py Extension:
	  $adddj [role]
	   └─ Adds a new role to the dj list (bot-admin only).
	  $listdj 
	   └─ Lists dj roles and id's.
	  $removedj [role]
	   └─ Removes a role from the dj list (bot-admin only).
	  $ytlist [yes_no]
	   └─ Gets or sets whether or not the server will show a list of options when searc...

## Debugging
####	Debugging Cog (9 commands) - Debugging.py Extension:
	  $clean [messages] [chan]
	   └─ Cleans the passed number of messages from the given channel (admin only).
	  $cleardebug 
	   └─ Deletes the debug.txt file (owner only).
	  $heartbeat 
	   └─ Write to the console and attempt to send a message (owner only).
	  $logdisable [options]
	   └─ Disables the passed, comma-delimited log vars.
	  $logenable [options]
	   └─ Enables the passed, comma-delimited log vars.
	  $logging 
	   └─ Outputs whether or not we're logging is enabled (bot-admin only).
	  $logpreset [preset]
	   └─ Can select one of 4 available presets - off, quiet, normal, verbose (bot-admi...
	  $setdebug [debug]
	   └─ Turns on/off debugging (owner only - always off by default).
	  $setlogchannel [channel]
	   └─ Sets the channel for Logging (bot-admin only).

## DisableCommand
####	DisableCommand Cog (9 commands) - DisableCommand.py Extension:
	  $adminallow [yes_no]
	   └─ Sets whether admins can access disabled commands (admin-only).
	  $badminallow [yes_no]
	   └─ Sets whether bot-admins can access disabled commands (admin-only).
	  $disable [command_or_cog_name]
	   └─ Disables the passed command or all commands in the passed cog (admin-only).  ...
	  $disableall 
	   └─ Disables all enabled commands outside this module (admin-only).
	  $disabledreact [yes_no]
	   └─ Sets whether the bot reacts to disabled commands when attempted (admin-only).
	  $enable [command_or_cog_name]
	   └─ Enables the passed command or all commands in the passed cog (admin-only).  C...
	  $enableall 
	   └─ Enables all disabled commands (admin-only).
	  $isdisabled [command_or_cog_name]
	   └─ Outputs whether the passed command - or all commands in a passed cog are disa...
	  $listdisabled 
	   └─ Lists all disabled commands (admin-only).

## DrBeer
####	DrBeer Cog (1 command) - DrBeer.py Extension:
	  $drbeer 
	   └─ Put yourself in your place.

## EightBall
####	EightBall Cog (1 command) - EightBall.py Extension:
	  $eightball [question]
	   └─ Get some answers.

## Emoji
####	Emoji Cog (1 command) - Emoji.py Extension:
	  $emoji [emoji]
	   └─ Outputs the passed emoji... but bigger!

## Encode
####	Encode Cog (10 commands) - Encode.py Extension:
	  $binint [input_binary]
	   └─ Converts the input binary to its integer representation.
	  $binstr [input_binary]
	   └─ Converts the input binary to its string representation.
	  $color [value]
	   └─ View info on a rgb, hex or cmyk color and their
	  $dechex [input_dec]
	   └─ Converts an int to hex.
	  $encode [from_type] [to_type] [value]
	   └─ Data converter from ascii <--> hex <--> base64.
	  $hexdec [input_hex]
	   └─ Converts hex to decimal.
	  $hexswap [input_hex]
	   └─ Byte swaps the passed hex value.
	  $intbin [input_int]
	   └─ Converts the input integer to its binary representation.
	  $slide [input_hex]
	   └─ Calculates your slide value for Clover based on an input address (in hex).
	  $strbin [input_string]
	   └─ Converts the input string to its binary representation.

## Example
####	Example Cog (4 commands) - Example.py Extension:
	  $add <left> <right>
	   └─ Adds two numbers together.
	  $choose [choices...]
	   └─ Chooses between multiple choices.
	  $joined [member]
	   └─ Says when a member joined.
	  $roll [dice=1d20]
	   └─ Rolls a dice in NdN±Na/d format.

## Face
####	Face Cog (4 commands) - Face.py Extension:
	  $lastlenny 
	   └─ Who Lenny'ed last?
	  $lastshrug 
	   └─ Who shrugged last?
	  $lenny [message]
	   └─ Give me some Lenny.
	  $shrug [message]
	   └─ Shrug it off.

## Feed
####	Feed Cog (8 commands) - Feed.py Extension:
	  $feed [food]
	   └─ Feed the bot some xp!
	  $hunger 
	   └─ How hungry is the bot?
	  $ignoredeath [yes_no]
	   └─ Sets whether the bot ignores its own death and continues to respond post-mort...
	  $iskill 
	   └─ Check the ded of the bot.
	  $kill 
	   └─ Kill the bot... you heartless soul.
	  $killrole 
	   └─ Lists the required role to kill/resurrect the bot.
	  $resurrect 
	   └─ Restore life to the bot.  What magic is this?
	  $setkillrole [role]
	   └─ Sets the required role ID to add/remove hacks (admin only).

## Fliptime
####	Fliptime Cog (1 command) - Fliptime.py Extension:
	  $tableflip [yes_no]
	   └─ Turns on/off table flip muting (bot-admin only; always off by default).

## GameLookup
####	GameLookup Cog (1 command) - GameLookup.py Extension:
	  $gamelookup <game>
	   └─ Help not available...

## Giphy
####	Giphy Cog (4 commands) - Giphy.py Extension:
	  $addgif [role]
	   └─ Adds a new role to the gif list (admin only).
	  $gif [gif]
	   └─ Search for some giphy!
	  $listgif 
	   └─ Lists gif roles and id's.
	  $removegif [role]
	   └─ Removes a role from the gif list (admin only).

## Groot
####	Groot Cog (1 command) - Groot.py Extension:
	  $groot 
	   └─ Who... who are you?

## Help
####	Help Cog (3 commands) - Help.py Extension:
	  $dumphelp [tab_indent_count]
	   └─ Dumps a timpestamped, formatted list of commands and descriptions into the sa...
	  $dumpmarkdown 
	   └─ Dumps a timpestamped, markdown-formatted list of commands and descriptions in...
	  $help [command]
	   └─ Lists the bot's commands and cogs.

## Humor
####	Humor Cog (8 commands) - Humor.py Extension:
	  $fart 
	   └─ PrincessZoey :P
	  $french 
	   └─ Speaking French... probably...
	  $german 
	   └─ Speaking German... probably...
	  $holy [subject]
	   └─ Time to backup the Batman!
	  $meme [template_id] [text_zero] [text_one]
	   └─ Generate Memes!  You can get a list of meme templates with the memetemps comm...
	  $memetemps 
	   └─ Get Meme Templates
	  $poke [url]
	   └─ Pokes the passed url/user/uploaded image.
	  $zalgo [message]
	   └─ Ỉ s̰hͨo̹u̳lͪd͆ r͈͍e͓̬a͓͜lͨ̈l̘̇y̡͟ h͚͆a̵͢v͐͑eͦ̓ i͋̍̕n̵̰ͤs͖̟̟t͔ͤ̉ǎ͓͐ḻ̪ͨl̦͒̂e...

## Hw
####	Hw Cog (12 commands) - Hw.py Extension:
	  $cancelhw 
	   └─ Cancels a current hardware session.
	  $delhw [build]
	   └─ Removes a build from your build list.
	  $edithw [build]
	   └─ Edits a build from your build list.
	  $gethw [user] [search]
	   └─ Searches the user's hardware for a specific search term.
	  $hw [user] [build]
	   └─ Lists the hardware for either the user's default build - or the passed build.
	  $listhw [user]
	   └─ Lists the builds for the specified user - or yourself if no user passed.
	  $mainhw [build]
	   └─ Sets a new main build from your build list.
	  $newhw 
	   └─ Initiate a new-hardware conversation with the bot.  The hardware added will a...
	  $pcpp [url] [style] [escape]
	   └─ Convert a pcpartpicker.com link into markdown parts. Available styles: normal...
	  $rawhw [user] [build]
	   └─ Lists the raw markdown for either the user's default build - or the passed bu...
	  $renhw [build]
	   └─ Renames a build from your build list.
	  $sethwchannel [channel]
	   └─ Sets the channel for hardware (admin only).

## IntelArk
####	IntelArk Cog (1 command) - IntelArk.py Extension:
	  $iark [text]
	   └─ Search Ark for Intel CPU info.

## Invite
####	Invite Cog (9 commands) - Invite.py Extension:
	  $approvejoin [server_id]
	   └─ Temporarily allows the bot to join the passed server id or join url (owner-on...
	  $block [server]
	   └─ Blocks the bot from joining a server - takes either a name or an id (owner-on...
	  $blocked 
	   └─ Lists all blocked servers and owners (owner-only).
	  $canjoin [yes_no]
	   └─ Sets whether the bot is allowed to join new servers (owner-only and enabled b...
	  $invite [invite_url]
	   └─ Outputs a url you can use to invite me to your server.
	  $requestjoin [invite_url]
	   └─ Forwards the invite url to the bot's owners for review.
	  $revokejoin [server_id]
	   └─ Revokes a previously approved temporary join (owner-only).
	  $unblock [server]
	   └─ Unblocks a server or owner (owner-only).
	  $unblockall 
	   └─ Unblocks all blocked servers and owners (owner-only).

## Jpeg
####	Jpeg Cog (1 command) - Jpeg.py Extension:
	  $jpeg [url]
	   └─ MOAR JPEG!  Accepts a url - or picks the first attachment.

## LangFilter
####	LangFilter Cog (5 commands) - LangFilter.py Extension:
	  $addfilter [words]
	   └─ Adds comma delimited words to the word list (bot-admin only).
	  $clearfilter 
	   └─ Empties the list of words that will be filtered (bot-admin only).
	  $dumpfilter 
	   └─ Saves the filtered word list to a text file and uploads it to the requestor (...
	  $listfilter 
	   └─ Prints out the list of words that will be filtered (bot-admin only).
	  $remfilter [words]
	   └─ Removes comma delimited words from the word list (bot-admin only).

## Lists
####	Lists Cog (22 commands) - Lists.py Extension:
	  $addhack [name] [hack]
	   └─ Add a hack to the hack list.
	  $addlink [name] [link]
	   └─ Add a link to the link list.
	  $hack [name]
	   └─ Retrieve a hack from the hack list.
	  $hackinfo [name]
	   └─ Displays info about a hack from the hack list.
	  $hackrole 
	   └─ Lists the required role to add hacks.
	  $hacks 
	   └─ List all hacks in the hack list.
	  $lastonline [member]
	   └─ Lists the last time a user was online if known.
	  $link [name]
	   └─ Retrieve a link from the link list.
	  $linkinfo [name]
	   └─ Displays info about a link from the link list.
	  $linkrole 
	   └─ Lists the required role to add links.
	  $links 
	   └─ List all links in the link list.
	  $online 
	   └─ Lists the number of users online.
	  $parts [member]
	   └─ Retrieve a member's parts list. DEPRECATED - Use hw instead.
	  $partstemp 
	   └─ Gives a copy & paste style template for setting a parts list.
	  $rawhack [name]
	   └─ Retrieve a hack's raw markdown from the hack list.
	  $rawhacks 
	   └─ List raw markdown of all hacks in the hack list.
	  $rawlink [name]
	   └─ Retrieve a link's raw markdown from the link list.
	  $rawlinks 
	   └─ List raw markdown of all links in the link list.
	  $rawparts [member]
	   └─ Retrieve the raw markdown for a member's parts list. DEPRECATED - Use rawhw i...
	  $removehack [name]
	   └─ Remove a hack from the hack list.
	  $removelink [name]
	   └─ Remove a link from the link list.
	  $setparts [parts]
	   └─ Set your own parts - can be a url, formatted text, or nothing to clear. DEPRE...

## MadLibs
####	MadLibs Cog (1 command) - MadLibs.py Extension:
	  $madlibs 
	   └─ Let's play MadLibs!

## Morse
####	Morse Cog (3 commands) - Morse.py Extension:
	  $morse [content]
	   └─ Converts ascii to morse code.  Accepts a-z and 0-9.  Each letter is comprised...
	  $morsetable [num_per_row]
	   └─ Prints out the morse code lookup table.
	  $unmorse [content]
	   └─ Converts morse code to ascii.  Each letter is comprised of "-" or "." and sep...

## Music
####	Music Cog (16 commands) - Music.py Extension:
	  $autodeleteafter [seconds]
	   └─ Lists or sets the current delay before auto-deleting music related messages (...
	  $join [channel]
	   └─ Joins a voice channel.
	  $pause 
	   └─ Pauses the currently playing song.
	  $paused [moons]
	   └─ Lists whether or not the player is paused.  Synonym of the playing command.
	  $play [url]
	   └─ Plays from a url (almost anything youtube_dl supports) or resumes a currently...
	  $playing [moons]
	   └─ Lists the currently playing song if any.
	  $playingin 
	   └─ Shows the number of servers the bot is currently playing music in.
	  $playlist 
	   └─ Lists the queued songs in the playlist.
	  $repeat [yes_no]
	   └─ Checks or sets whether to repeat the current playlist.
	  $resume 
	   └─ Resumes the song if paused.
	  $skip 
	   └─ Adds your vote to skip the current song.  50% or more of the non-bot users ne...
	  $stop 
	   └─ Stops and disconnects the bot from voice.
	  $unplay [song_number]
	   └─ Removes the passed song number from the queue.  You must be the requestor, or...
	  $unqueue 
	   └─ Removes all songs you've added from the queue (does not include the currently...
	  $volume [volume]
	   └─ Changes the player's volume (0-100).
	  $yt [search]
	   └─ Searches youtube for the passed terms and posts a link to the first hit.

## OfflineUser
####	OfflineUser Cog (1 command) - OfflineUser.py Extension:
	  $remindoffline [yes_no]
	   └─ Sets whether to inform users that pinged members are offline or not.

## PciUsb
####	PciUsb Cog (2 commands) - PciUsb.py Extension:
	  $pci [ven_dev]
	   └─ Searches pci-ids.ucw.cz for the passed PCI ven:dev id.
	  $usb [ven_dev]
	   └─ Searches usb-ids.gowdy.us for the passed USB ven:dev id.

## Plist
####	Plist Cog (2 commands) - Plist.py Extension:
	  $nvweb [os_build]
	   └─ Prints the download url for the passed OS build number (if it exists).  If no...
	  $plist [url]
	   └─ Validates plist file structure.  Accepts a url - or picks the first attachment.

## Printer
####	Printer Cog (2 commands) - Printer.py Extension:
	  $print [url]
	   └─ DOT MATRIX.  Accepts a url - or picks the first attachment.
	  $printavi [member]
	   └─ Returns a url to the passed member's avatar.

## Profile
####	Profile Cog (7 commands) - Profile.py Extension:
	  $addprofile [name] [link]
	   └─ Add a profile to your profile list.
	  $profile [member] [name]
	   └─ Retrieve a profile from the passed user's profile list.
	  $profileinfo [member] [name]
	   └─ Displays info about a profile from the passed user's profile list.
	  $profiles [member]
	   └─ List all profiles in the passed user's profile list.
	  $rawprofile [member] [name]
	   └─ Retrieve a profile's raw markdown from the passed user's profile list.
	  $rawprofiles [member]
	   └─ List all profiles' raw markdown in the passed user's profile list.
	  $removeprofile [name]
	   └─ Remove a profile from your profile list.

## Promote
####	Promote Cog (4 commands) - Promote.py Extension:
	  $demote [member]
	   └─ Auto-removes the required xp to demote the passed user to the previous role (...
	  $demoteto [member] [role]
	   └─ Auto-removes the required xp to demote the passed user to the passed role (ad...
	  $promote [member]
	   └─ Auto-adds the required xp to promote the passed user to the next role (admin ...
	  $promoteto [member] [role]
	   └─ Auto-adds the required xp to promote the passed user to the passed role (admi...

## Quote
####	Quote Cog (6 commands) - Quote.py Extension:
	  $clearquotereaction 
	   └─ Clears the trigger reaction for quoting messages (admin only).
	  $getquotereaction 
	   └─ Displays the quote reaction if there is one.
	  $quoteadminonly [yes_no]
	   └─ Sets whether only admins/bot-admins can quote or not (bot-admin only).
	  $quotechannel 
	   └─ Prints the current quote channel.
	  $setquotechannel [channel]
	   └─ Sets the channel for quoted messages or disables it if no channel sent (admin...
	  $setquotereaction 
	   └─ Sets the trigger reaction for quoting messages (bot-admin only).

## RateLimit
####	RateLimit Cog (1 command) - RateLimit.py Extension:
	  $ccooldown [delay]
	   └─ Sets the cooldown in seconds between each command (owner only).

## Reddit
####	Reddit Cog (31 commands) - Reddit.py Extension:
	  $abandoned 
	   └─ Get something abandoned to look at.
	  $answer 
	   └─ Spout out some interstellar answering... ?
	  $aww 
	   └─ Whenever you're down - uppify.
	  $battlestation 
	   └─ Let's look at some pretty stuff.
	  $brainfart 
	   └─ Spout out some uh... intellectual brilliance...
	  $cablefail 
	   └─ Might as well be a noose...
	  $carmod 
	   └─ Marvels of modern engineering.
	  $dankmeme 
	   └─ Only the dankest.
	  $dirtyjoke 
	   └─ Let's see if reddit can be dir-... oh... uh.. funny... (bot-admin only)
	  $dragon 
	   └─ From the past - when great winged beasts soared the skies.
	  $earthporn 
	   └─ Earth is good.
	  $joke 
	   └─ Let's see if reddit can be funny...
	  $lpt 
	   └─ Become a pro - AT LIFE.
	  $macsetup 
	   └─ Feast your eyes upon these setups.
	  $meirl 
	   └─ Me in real life.
	  $nocontext 
	   └─ Spout out some intersexual brilliance.
	  $nosleep 
	   └─ I hope you're not tired...
	  $pun 
	   └─ I don't know, don't ask...
	  $question 
	   └─ Spout out some interstellar questioning... ?
	  $randomcat 
	   └─ Meow.
	  $randomdog 
	   └─ Bark if you know whassup.
	  $redditimage [subreddit]
	   └─ Try to grab an image from an image-based subreddit.
	  $ruser [user_name]
	   └─ Gets some info on the passed username - attempts to use your username if none...
	  $shittybattlestation 
	   └─ Let's look at some shitty stuff.
	  $shittylpt 
	   └─ Your advise is bad, and you should feel bad.
	  $software 
	   └─ I uh... I wrote it myself.
	  $starterpack 
	   └─ Starterpacks.
	  $techsupport 
	   └─ Tech support irl.
	  $thinkdeep 
	   └─ Spout out some intellectual brilliance.
	  $wallpaper 
	   └─ Get something pretty to look at.
	  $withcontext 
	   └─ Spout out some contextual brilliance.

## Remind
####	Remind Cog (3 commands) - Remind.py Extension:
	  $clearmind [index]
	   └─ Clear the reminder index passed - or all if none passed.
	  $reminders [member]
	   └─ List up to 10 pending reminders - pass a user to see their reminders.
	  $remindme [message] [endtime]
	   └─ Set a reminder.  If the message contains spaces, it must be wrapped in quotes.

## Search
####	Search Cog (8 commands) - Search.py Extension:
	  $aol [query]
	   └─ The OG search engine.
	  $ask [query]
	   └─ Jeeves, please answer these questions.
	  $bing [query]
	   └─ Get some uh... more searching done.
	  $convert [amount] [frm] [to]
	   └─ convert currencies
	  $duck [query]
	   └─ Duck Duck... GOOSE.
	  $google [query]
	   └─ Get some searching done.
	  $searchsite [category_name] [query]
	   └─ Search corpnewt.com forums.
	  $yahoo [query]
	   └─ Let Yahoo! answer your questions.

## SecretSanta
####	SecretSanta Cog (11 commands) - SecretSanta.py Extension:
	  $allowss [yes_no]
	   └─ Sets whether the Secret Santa module is enabled (owner only; always off by de...
	  $getssrole 
	   └─ Lists the current Secret Santa role.
	  $rawssmessage 
	   └─ Prints the raw markdown for the Secret Santa channel create message (bot-admi...
	  $setssmessage [message]
	   └─ Sets the Secret Santa channel create message (bot-admin only). 
	  $setssrole [role]
	   └─ Sets the Secret Santa role, or clears it if no role passed (bot-admin only).
	  $ssapplyreport [url]
	   └─ Applies the passed ss.json file's settings and gives the Secret Santa channel...
	  $sscreatechannels [category]
	   └─ Creates the private channels for all users with the Secret Santa role under t...
	  $ssgenreport [category]
	   └─ Randomly pairs users for Secret Santa and uploads a ss.json report (bot-admin...
	  $ssremovechannels [category]
	   └─ Removes all Secret Santa channels under a given category whose names correspo...
	  $ssrevert [category]
	   └─ Returns ownership of the Secret Santa channels to their original owners if fo...
	  $testssmessage 
	   └─ Prints the current Secret Santa channel create message (bot-admin only).

## Server
####	Server Cog (7 commands) - Server.py Extension:
	  $autopcpp [setting]
	   └─ Sets the bot's auto-pcpartpicker markdown if found in messages (admin-only). ...
	  $dumpservers 
	   └─ Dumps a timpestamped list of servers into the same directory as the bot (owne...
	  $getprefix 
	   └─ Output's the server's prefix - custom or otherwise.
	  $info 
	   └─ Displays the server info if any.
	  $leaveserver [targetServer]
	   └─ Leaves a server - can take a name or id (owner only).
	  $setinfo [word]
	   └─ Sets the server info (admin only).
	  $setprefix [prefix]
	   └─ Sets the bot's prefix (admin only).

## ServerStats
####	ServerStats Cog (15 commands) - ServerStats.py Extension:
	  $allmessages 
	   └─ Lists the number of messages I've seen on all severs so far. (only applies af...
	  $bottomservers [number=10]
	   └─ Lists the bottom servers I'm connected to ordered by population - default is ...
	  $firstjoins [number=10]
	   └─ Lists the first users to join - default is 10, max is 25.
	  $firstservers [number=10]
	   └─ Lists the first servers I've joined - default is 10, max is 25.
	  $joinedatpos <position>
	   └─ Lists the user that joined at the passed position.
	  $joinpos [member]
	   └─ Tells when a user joined compared to other users.
	  $listbots [guild_name]
	   └─ Lists up to the first 20 bots of the current or passed server.
	  $listservers [number=10]
	   └─ Lists the servers I'm connected to - default is 10, max is 50.
	  $messages 
	   └─ Lists the number of messages I've seen on this sever so far. (only applies af...
	  $recentjoins [number=10]
	   └─ Lists the most recent users to join - default is 10, max is 25.
	  $recentservers [number=10]
	   └─ Lists the most recent users to join - default is 10, max is 25.
	  $serverinfo [guild_name]
	   └─ Lists some info about the current or passed server.
	  $sharedservers [member]
	   └─ Lists how many servers you share with the bot.
	  $topservers [number=10]
	   └─ Lists the top servers I'm connected to ordered by population - default is 10,...
	  $users 
	   └─ Lists the total number of users on all servers I'm connected to.

## Settings
####	Settings Cog (13 commands) - Settings.py Extension:
	  $addowner [member]
	   └─ Adds an owner to the owner list.  Can only be done by a current owner.
	  $claim 
	   └─ Claims the bot if disowned - once set, can only be changed by the current owner.
	  $disown 
	   └─ Revokes all ownership of the bot.
	  $flush 
	   └─ Flush the bot settings to disk (admin only).
	  $getsstat [stat]
	   └─ Gets a server stat (admin only).
	  $getstat [stat] [member]
	   └─ Gets the value for a specific stat for the listed member (case-sensitive).
	  $ownerlock 
	   └─ Locks/unlocks the bot to only respond to the owner (owner-only... ofc).
	  $owners 
	   └─ Lists the bot's current owners.
	  $prune 
	   └─ Iterate through all members on all connected servers and remove orphaned sett...
	  $prunelocalsettings 
	   └─ Compares the current server's settings to the default list and removes any no...
	  $prunesettings 
	   └─ Compares all connected servers' settings to the default list and removes any ...
	  $remowner [member]
	   └─ Removes an owner from the owner list.  Can only be done by a current owner.
	  $setsstat [stat] [value]
	   └─ Sets a server stat (admin only).

## Setup
####	Setup Cog (1 command) - Setup.py Extension:
	  $setup 
	   └─ Runs first-time setup (server owner only).

## Spooktober
####	Spooktober Cog (1 command) - Spooktober.py Extension:
	  $spooking [yes_no]
	   └─ Enables/Disables reacting 🎃 to every message on Halloween

## Stream
####	Stream Cog (8 commands) - Stream.py Extension:
	  $addstreamer [member]
	   └─ Adds the passed member to the streamer list (bot-admin only).
	  $rawstream [message]
	   └─ Displays the raw markdown for the stream announcement message (bot-admin only).
	  $remstreamer [member]
	   └─ Removes the passed member from the streamer list (bot-admin only).
	  $setstream [message]
	   └─ Sets the stream announcement message (bot-admin only).
	  $setstreamchannel [channel]
	   └─ Sets the channel for the stream announcements (bot-admin only).
	  $streamchannel 
	   └─ Displays the channel for the stream announcements - if any.
	  $streamers 
	   └─ Lists the current members in the streamer list.
	  $teststream [message]
	   └─ Tests the stream announcement message (bot-admin only).

## Strike
####	Strike Cog (12 commands) - Strike.py Extension:
	  $addban [member]
	   └─ Adds the passed user to the ban list (bot-admin only).
	  $addkick [member]
	   └─ Adds the passed user to the kick list (bot-admin only).
	  $isbanned [member]
	   └─ Lists whether the user is in the ban list.
	  $iskicked [member]
	   └─ Lists whether the user is in the kick list.
	  $removeban [member]
	   └─ Removes the passed user from the ban list (bot-admin only).
	  $removekick [member]
	   └─ Removes the passed user from the kick list (bot-admin only).
	  $removestrike [member]
	   └─ Removes a strike given to a member (bot-admin only).
	  $setstrikelevel [member] [strikelevel]
	   └─ Sets the strike level of the passed user (bot-admin only).
	  $setstrikelimit [limit]
	   └─ Sets the number of strikes before advancing to the next consequence (bot-admi...
	  $strike [member] [days] [message]
	   └─ Give a user a strike (bot-admin only).
	  $strikelimit 
	   └─ Lists the number of strikes before advancing to the next consequence.
	  $strikes [member]
	   └─ Check a your own, or another user's total strikes (bot-admin needed to check ...

## Tags
####	Tags Cog (9 commands) - Tags.py Extension:
	  $addtag [name] [tag]
	   └─ Add a tag to the tag list.
	  $rawtag [name]
	   └─ Retrieve a tag's raw markdown from the tag list.
	  $rawtags 
	   └─ List raw markdown of all tags in the tags list.
	  $removetag [name]
	   └─ Remove a tag from the tag list.
	  $settagrole [role]
	   └─ Sets the required role ID to add/remove tags (admin only).
	  $tag [name]
	   └─ Retrieve a tag from the tag list.
	  $taginfo [name]
	   └─ Displays info about a tag from the tag list.
	  $tagrole 
	   └─ Lists the required role to add tags.
	  $tags 
	   └─ List all tags in the tags list.

## Telephone
####	Telephone Cog (9 commands) - Telephone.py Extension:
	  $call [number]
	   └─ Calls the passed number.  Can use *67 to hide your identity - or *69 to conne...
	  $callerid 
	   └─ Reveals the last number to call regardless of *67 settings (bot-admin only).
	  $phonebook [look_up]
	   └─ Lets you page through the phonebook - or optionally lets you search for a ser...
	  $settelechannel [channel]
	   └─ Sets the channel for telephone commands - or disables that if nothing is pass...
	  $teleblock [guild_name]
	   └─ Blocks all tele-numbers associated with the passed guild (bot-admin only).
	  $teleblocks 
	   └─ Lists guilds with blocked tele-numbers.
	  $telechannel 
	   └─ Prints the current channel for telephone commands.
	  $telenumber 
	   └─ Prints your telephone number.
	  $teleunblock [guild_name]
	   └─ Unblocks all tele-numbers associated with the passed guild (bot-admin only).

## TempRole
####	TempRole Cog (10 commands) - TempRole.py Extension:
	  $addtemprole [role]
	   └─ Adds a new role to the temp role list (admin only).
	  $autotemp [role]
	   └─ Sets the temp role to apply to each new user that joins.
	  $getautotemp 
	   └─ Gets the temp role applied to each new user that joins.
	  $hastemp [member]
	   └─ Displays any temp roles the passed user has, and the remaining time.
	  $listtemproles 
	   └─ Lists all roles for the temp role system.
	  $removetemprole [role]
	   └─ Removes a role from the temp role list (admin only).
	  $temp [member] [role] [cooldown]
	   └─ Gives the passed member the temporary role for the passed amount of time - ne...
	  $temppm [yes_no]
	   └─ Sets whether to inform users that they've been given a temp role.
	  $temptime [minutes]
	   └─ Sets the number of minutes for the temp role - must be greater than 0 (admin-...
	  $untemp [member] [role]
	   └─ Removes the passed temp role from the passed user (bot-admin only).

## Time
####	Time Cog (6 commands) - Time.py Extension:
	  $listtz [tz_search]
	   └─ List all the supported TimeZones in PM.
	  $offset [member]
	   └─ See a member's UTC offset.
	  $setoffset [offset]
	   └─ Set your UTC offset.
	  $settz [tz]
	   └─ Sets your TimeZone - Overrides your UTC offset - and accounts for DST.
	  $time [offset]
	   └─ Get UTC time +- an offset.
	  $tz [member]
	   └─ See a member's TimeZone.

## Translate
####	Translate Cog (2 commands) - Translate.py Extension:
	  $langlist 
	   └─ Lists available languages.
	  $tr [translate]
	   └─ Translate some stuff!  Takes a phrase, the from language identifier (optional...

## Turret
####	Turret Cog (1 command) - Turret.py Extension:
	  $turret 
	   └─ Now you're thinking with - wait... uh.. turrets?

## Uptime
####	Uptime Cog (1 command) - Uptime.py Extension:
	  $uptime 
	   └─ Lists the bot's uptime.

## UrbanDict
####	UrbanDict Cog (2 commands) - UrbanDict.py Extension:
	  $define [word]
	   └─ Gives the definition of the word passed.
	  $randefine 
	   └─ Gives a random word and its definition.

## UserRole
####	UserRole Cog (11 commands) - UserRole.py Extension:
	  $addrole [role]
	   └─ Adds a role from the user role list to your roles.  You can have multiples at...
	  $adduserrole [role]
	   └─ Adds a new role to the user role system (admin only).
	  $clearroles 
	   └─ Removes all user roles from your roles.
	  $isurblocked [member]
	   └─ Outputs whether or not the passed user is blocked from the UserRole module.
	  $listuserroles 
	   └─ Lists all roles for the user role system.
	  $oneuserrole [yes_no]
	   └─ Turns on/off one user role at a time (bot-admin only; always on by default).
	  $removeuserrole [role]
	   └─ Removes a role from the user role system (admin only).
	  $remrole [role]
	   └─ Removes a role from the user role list from your roles.
	  $setrole [role]
	   └─ Sets your role from the user role list.  You can only have one at a time.
	  $urblock [member]
	   └─ Blocks a user from using the UserRole system and removes applicable roles (bo...
	  $urunblock [member]
	   └─ Unblocks a user from the UserRole system (bot-admin only).

## VoteKick
####	VoteKick Cog (13 commands) - VoteKick.py Extension:
	  $setvkchannel [channel]
	   └─ Sets which channel then mention posts to when enough votes against a user are...
	  $setvkmention [user_or_role]
	   └─ Sets which user or role is mentioned when enough votes against a user are rea...
	  $vk [user] [server]
	   └─ Places your vote to have the passed user kicked.
	  $vkanon [yes_no]
	   └─ Sets whether vote messages are removed after voting (bot-admin only; always o...
	  $vkchannel 
	   └─ Gets which channel then mention posts to when enough votes against a user are...
	  $vkclear [user]
	   └─ Clears the votes against the passed user (bot-admin only).
	  $vkexpiretime [the_time]
	   └─ Sets the amount of time before a vote expires.  0 or less will make them perm...
	  $vkinfo 
	   └─ Lists the vote-kick info.
	  $vkmention 
	   └─ Gets which user or role is mentioned when enough votes against a user are rea...
	  $vkmutetime [the_time]
	   └─ Sets the number of time a user is muted when the mute votes are reached - 0 o...
	  $vks [user]
	   └─ Lists the vote count of the passed user (bot-admin only) or the author if no ...
	  $vktomention [number_of_votes]
	   └─ Sets the number of votes before the selected role or user is mentioned.  Anyt...
	  $vktomute [number_of_votes]
	   └─ Sets the number of votes before a user is muted.  Anything less than 1 will d...

## Weather
####	Weather Cog (3 commands) - Weather.py Extension:
	  $forecast [city_name]
	   └─ Gets some weather, for 5 days or whatever.
	  $tconvert [temp] [from_type] [to_type]
	   └─ Converts between Fahrenheit, Celsius, and Kelvin.  From/To types can be:
	  $weather [city_name]
	   └─ Gets some weather.

## Welcome
####	Welcome Cog (7 commands) - Welcome.py Extension:
	  $rawgoodbye [member]
	   └─ Prints the current goodbye message's markdown (bot-admin only).
	  $rawwelcome [member]
	   └─ Prints the current welcome message's markdown (bot-admin only).
	  $setgoodbye [message]
	   └─ Sets the goodbye message for your server (bot-admin only).
	  $setwelcome [message]
	   └─ Sets the welcome message for your server (bot-admin only). 
	  $setwelcomechannel [channel]
	   └─ Sets the channel for the welcome and goodbye messages (bot-admin only).
	  $testgoodbye [member]
	   └─ Prints the current goodbye message (bot-admin only).
	  $testwelcome [member]
	   └─ Prints the current welcome message (bot-admin only).

## Wiki
####	Wiki Cog (1 command) - Wiki.py Extension:
	  $wiki [search]
	   └─ Search Wikipedia!

## Xp
####	Xp Cog (11 commands) - Xp.py Extension:
	  $bottomxp [total=10]
	   └─ List the bottom xp-holders (max of 50).
	  $defaultrole 
	   └─ Lists the default role that new users are assigned.
	  $gamble [bet]
	   └─ Gamble your xp reserves for a chance at winning xp!
	  $leaderboard [total=10]
	   └─ List the top xp-holders (max of 50).
	  $listxproles 
	   └─ Lists all roles, id's, and xp requirements for the xp promotion/demotion system.
	  $rank [member]
	   └─ Say the highest rank of a listed member.
	  $recheckrole [user]
	   └─ Re-iterate through all members and assign the proper roles based on their xp ...
	  $recheckroles 
	   └─ Re-iterate through all members and assign the proper roles based on their xp ...
	  $stats [member]
	   └─ List the xp and xp reserve of a listed member.
	  $xp [member] [xpAmount]
	   └─ Gift xp to other members.
	  $xpinfo 
	   └─ Gives a quick rundown of the xp system.

## XpBlock
####	XpBlock Cog (4 commands) - XpBlock.py Extension:
	  $listxpblock 
	   └─ Lists xp blocked users and roles.
	  $xpblock [user_or_role]
	   └─ Adds a new user or role to the xp block list (bot-admin only).
	  $xpunblock [user_or_role]
	   └─ Removes a user or role from the xp block list (bot-admin only).
	  $xpunblockall 
	   └─ Removes all users and roles from the xp block list (bot-admin only).

## XpStack
####	XpStack Cog (5 commands) - XpStack.py Extension:
	  $checkxp 
	   └─ Displays the last xp transactions (bot-admin only).
	  $clearallxp 
	   └─ Clears all xp transactions from the transaction list for all servers (owner-o...
	  $clearxp 
	   └─ Clears the xp transaction list (bot-admin only).
	  $setxpcount [count]
	   └─ Sets the number of xp transactions to keep (default is 10).
	  $xpcount [count]
	   └─ Returns the number of xp transactions to keep (default is 10).
