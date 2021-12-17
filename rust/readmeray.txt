in rust cargo is the thing that does a lot of shit
-> cargo new new-project-name 
-> cargo build
-> cargo run 
etc
etc

add dependencies in the Cargo.taml file which is the manifest file then you do cargo build to load them in. This creates the Cargo.lock file which logs the exact version of the dependencies being used locally 

Write use in 