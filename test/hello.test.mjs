import { test } from "node:test";
import assert from "node:assert/strict";
import { greet } from "../hello.mjs";

test("default greeting", () => assert.equal(greet(), "Hello, World!"));
test("named greeting", () => assert.equal(greet("Ada"), "Hello, Ada!"));
test("unicode name", () => assert.equal(greet("Çağrı"), "Hello, Çağrı!"));
